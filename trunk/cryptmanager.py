#!/usr/bin/python
# vim: set fileencoding=utf-8 :
# Copyright (C) 2007 Kévin Dunglas <dunglas@gmail.com>
#
# Authors:
#  Kévin Dunglas
#
# This program is a part of a the Google Summer Of Code 2007
# For futher information see :
# http://code.google.com/soc/ubuntu/appinfo.html?csaid=EF4FCF874D88234
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 59 Temple
# Place, Suite 330, Boston, MA 02111-1307 USA

import subprocess
import os
import hashlib
import shutil
import math

IMGDIR = os.environ['HOME'] + "/.config/cryptmanager/img"
BACKUP = os.environ['HOME'] + "/.config/cryptmanager/backup"
TMPDIR = "/tmp/cryptmanager"
DD = "/bin/dd"
LOSETUP = "/sbin/losetup"
CRYPTSETUP = "/sbin/cryptsetup"
FS = "ext3"
MKFS = "/sbin/mkfs." + FS
MOUNT = "/bin/mount"
UMOUNT = "/bin/umount"
# Use the UID of the real user (not sudo)
try:
    UID = os.environ["SUDO_UID"]
except KeyError:
    UID = os.environ["UID"]
try:
    GID = os.environ["SUDO_GID"]
except KeyError:
    GID = os.environ["GID"]


class IMGexists(Exception):
    def __str__(self):
        return "This is already a crypted folder"


class BadPassword(Exception):
    def __str__(self):
        return "The password is wrong"


class AlreadyExists(Exception):
    def __str__(self):
        return "This folder already exists"


class AlreadyOpened(Exception):
    def __str__(self):
            return "This folder is already opened"


class NoEcrypted(Exception):
    def __str__(self):
            return "This folder is not crypted"


class NotOpened(Exception):
    def __str__(self):
            return "This folder is not opened"
     
           
class LoError(Exception):
    def __str__(self):
            return "No loopback device available"


class NotDir(Exception):
    def __str__(self):
            return "This is not a directory"


class TooSmall(Exception):
    def __str__(self):
            return "Size too small"

      
class Util:
    """Utilities"""    
    def rm(self, path):
        """Remove recursively a directory"""
        if os.path.exists(path):
            shutil.rmtree(path)

    def fullpath(self, path):
        """Expand a path"""
        path = os.path.expanduser(path)
        path = os.path.realpath(path)
        path = os.path.normpath(path)
        return path
        
    def cp(self, src, dst):
        """Copy recursively"""
        if not os.path.exists(dst):
            os.makedirs(dst)
        for f in os.listdir(src):
            if os.path.isdir(os.path.join(src, f)):
                self.cp(os.path.join(src, f), os.path.join(dst, f))
            if os.path.isfile(os.path.join(src, f)):
                try:
                    shutil.copy2(os.path.join(src, f), os.path.join(dst, f))
                except OSError:
                    pass
    
    def du(self, path):
        """Calcul recursively the size of a repository in MB"""
        self.size = 0
        self.du2(path)
        return int(math.ceil(self.size / 1024 / 1024))
    
    def du2(self, path):
        for f in os.listdir(path):
            if os.path.isdir(os.path.join(path, f)):
                self.du2(os.path.join(path, f))
            if os.path.isfile(os.path.join(path, f)):
               self.size += os.path.getsize(s.path.join(path, f))
    
    def min_size(self, path, size):
        """Test if the crypted folder can contain the current data.
        Return 0 if the size is correct, the minimum size either"""
        cs = self.du(path) * 2
        if cs > size:
            return cs
        return 0

    def chown(self, path, uid, gid):
        """Change owner recursively"""
        for f in os.listdir(path):
            if os.path.isdir(os.path.join(path, f)):
                self.chown(os.path.join(path, f), uid, gid)
            if os.path.isfile(os.path.join(path, f)):
                os.lchown(os.path.join(path, f), uid, gid)

class Folders:
    """Folders list"""
    def __init__(self):
        self.li = []

    def add(self, folder):
        """Add a folder"""
        for f in self.li:
            if f.path == folder.path:
                raise AlreadyExists()
                return
        self.li.append(folder)
        
    def rem(self, folder):
        """Remove a folder"""
        for f in self.li:
            if f.path == folder.path:
                self.li.remove(f)
    
    def update(self, folder):
        """Update a folder"""
        self.rem(folder)
        self.add(folder)
    
    def get(self, path):
        """Get a folder"""
        path = Util().fullpath(path)
        for f in self.li:
            if f.path == path:
                return f
        raise NoEncrypted()
    
    def restore(self):
        """Restore the state of the folders (i.e: after a reboot)"""
        for f in self.li:
            if f.opened == True:
                if not os.path.exists ("/dev/mapper/" + f.digest):
                    f.opened = False
                    Manage(f).mount()
    
    def close_all(self):
        """Close all the open folders (i.e: before a reboot)"""
        for f in self.li:
            if f.opened:
                Manage(f).unmount()
    
    def clean(self):
        """Delete unused Folders and empty TMPDIR"""
        for f in self.li:
            if not os.path.exists(IMGDIR + "/" + f.digest):
                self.li.remove(f)

        if not os.path.exists(BACKUP):
            os.makedirs(BACKUP)

#        for f in os.listdir(IMGDIR):
#            if os.path.isfile(os.path.join(IMGDIR, f)):
#                ok = False
#                for fo in self.li:
#                    if os.path.join(IMGDIR, f) == fo.path:
#                        ok = True
#                if not ok:
#                    shutil.move(os.path.join(IMGDIR, f), os.path.join(BACKUP, f))
#        Util().rm(TMPDIR)


class Folder:
    """Folder information"""
    def __init__(self, path, size, loop=None):
        self.path = Util().fullpath(path)
        if not os.path.isdir(self.path):
               raise NotDir()
               return
        self.size = size
        self.digest = self.digest()
        self.loop = loop
        self.opened = False
        
    def __repr__(self):
        return repr(self.path)

    def digest(self):
        h = hashlib.sha256()
        h.update(self.path)
        return h.hexdigest()


class Test:
    def __init__(self, folder):
        """Encrypt a folder"""
        self.folder = folder


class Manage:
    """Operations on a folder"""
    def __init__(self, folder):
        self.folder = folder
        self.img = os.path.join(IMGDIR, folder.digest)
        self.mapper = "/dev/mapper/" + folder.digest

    def crypt(self, password):
        """Encrypt a folder"""
        # Create ~/.config/cryptmanager if needed
        # The disk images are stored here
        if not os.path.exists(IMGDIR):
            os.makedirs(IMGDIR)
            
        # Test if the encrypted folder can contain current data
        ms = Util().min_size(self.folder.path, self.folder.size)
        if ms != 0:
            raise TooSmall()
            return

        # Test if the disk images (sha256 hash of the path name) already exists
        if os.path.exists(self.img):
            raise IMGexists()
            return
        self.test_lo()
        # Create the disk image
        subprocess.check_call([DD, "if=/dev/zero", "of=" + self.img,\
            "bs=1M", "count=" + str(self.folder.size)])
      
        tmp = os.path.join(TMPDIR, self.folder.digest)
        # Delete /tmp/cryptmanager/DIGEST if already exists
        Util().rm(tmp)
        # Move the existing content in a tmp directory
        Util().cp(self.folder.path, tmp)
        Util().rm(self.folder.path)
        # Create the mount point if needed
        os.makedirs(self.folder.path)
        
        # Can also use Debian specific /sbin/luksformat to do next steps
        
        # Crypt the disk image
        self.losetup()
        p1 = subprocess.Popen(["echo", "\"" + password + "\""],\
            stdout=subprocess.PIPE)
        p2 = subprocess.Popen([CRYPTSETUP, "--batch-mode", "luksFormat",\
            self.folder.loop], stdin=p1.stdout, stdout=subprocess.PIPE)
        p2.communicate()[0]
        self.delete_lo()
        
        self.open_img(password)
            
        # Format the disk image
        subprocess.check_call([MKFS, self.mapper])
            
        self.close_img()
        self.mount(password)
        # Copy existing data in the crypted directory
        Util().cp(tmp, self.folder.path)
        Util().rm(tmp)
        self.unmount()

    def mount(self, password):
        """Mount an encrypted folder"""
        # if .crypt exists and contain a ref to ~/.crypt/XXX
        # this an unmounted crypted directory
        
        if self.folder.opened:
            raise AlreadyOpened()
            return
        try:
            self.open_img(password)
        except BadPassword:
            raise BadPassword()
            return
        # Maybe can we also use HAL and/or gnome-mount
        # Mount
        subprocess.check_call([MOUNT, self.mapper, self.folder.path])
        self.folder.opened = True
        Util().chown(self.folder.path, UID, GID)
        
        return self.folder

    def unmount(self):
        """Unmount an encrypted folder"""
        
        if not self.folder.opened:
            raise NotOpened()
            return

        # Unmount
        subprocess.check_call([UMOUNT, self.mapper])

        self.close_img()
        self.folder.opened = False
        
        return self.folder

    def decrypt(self, password):
        """Decrypt a folder"""
        tmp = os.path.join(TMPDIR, self.folder.digest)

        # Delete /tmp/cryptmanager/DIGEST if already exists
        Util().rm(tmp)

        try:
            self.mount(password)
        except AlreadyOpened:
            pass
        except BadPassword:
            raise BadPassword()
            return 
        Util().cp(self.folder.path, tmp)
        self.unmount()
        os.unlink(self.img)
        Util().cp(tmp, self.folder.path)
        Util().rm(tmp)

    def test_lo(self):
        """Test if a loopback device is available"""
        ret = subprocess.call ([LOSETUP, "-f"])
        if ret is not 0:
            raise LoError()

    def losetup(self):
        """Set up the loop device"""
        # Get the first unused /dev/loopX
        self.test_lo()
        p = os.popen (LOSETUP + " -f")
        for s in p:
            self.folder.loop = s.strip("\n")
        # Set up the loop device
        r = subprocess.call([LOSETUP, self.folder.loop, self.img])
        if r is not 0:
            raise LoError()

    def open_img(self, password):
        """Open the disk image"""
        self.losetup()
        p1 = subprocess.Popen(["echo", "\"" + password + "\""], \
            stdout=subprocess.PIPE)
        p2 = subprocess.Popen([CRYPTSETUP, "--batch-mode", "luksOpen", \
            self.folder.loop, self.folder.digest], stdin=p1.stdout, \
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        p2.communicate()
        if p2.returncode > 0:
            self.delete_lo()
            raise BadPassword()
        #subprocess.check_call([CRYPTSETUP, "luksOpen", self.folder.loop, \
        #self.folder.digest])

    def close_img(self):
        """Close the disk image"""
        subprocess.check_call([CRYPTSETUP, "luksClose", self.folder.digest])
        self.delete_lo()

    def delete_lo(self):
        """Delete the loop device"""
        subprocess.check_call([LOSETUP, "-d", self.folder.loop])
        self.folder.loop = None
