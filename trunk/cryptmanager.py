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

# http://forum.ubuntu-fr.org/viewtopic.php?pid=268552#p268552

TMPDIR = "/tmp/cryptmanager"
IMGDIR = os.environ['HOME'] + "/.config/cryptmanager/img"
DD = "/bin/dd"
LOSETUP = "/sbin/losetup"
CRYPTSETUP = "/sbin/cryptsetup"
MKFS = "/sbin/mkfs.ext3"
MOUNT = "/bin/mount"
UMOUNT = "/bin/umount"


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
            
class Util:
    def rm(self, path):
        """Remove recursivly a directory"""
        if os.path.exists(path):
            for root, dirs, files in os.walk(path, topdown=False):
                for name in files:
                    os.unlink(os.path.join(root, name))
                for name in dirs:
                    os.rmdir(os.path.join(root, name))

class Folders:
    def __init__(self):
        """Folders list"""
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


class Folder:
    def __init__(self, path, password=None, size=None, loop=None):
        """Folder information"""
        self.path = path
        self.password = password
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
        print self.folder.password


class Manage:
    def __init__(self, folder):
        self.folder = folder
        self.img = os.path.join(IMGDIR, folder.digest)
        self.mapper = "/dev/mapper/" + folder.digest

    def crypt(self):
        """Encrypt a folder"""
        # Create ~/.config/cryptmanager if needed
        # The disk images are stored here
        if not os.path.exists(IMGDIR):
            os.makedirs(IMGDIR)

        # Create the mount point if needed
        if not os.path.exists(self.folder.path):
            os.makedirs(self.folder.path)

        # Test if the disk images (sha256 hash of the path name) already exists
        if os.path.exists(self.img):
            raise IMGexists()
        else:
            # Create the disk image
            subprocess.check_call([DD, "if=/dev/zero", "of=" + self.img, "bs=1M", "count=" + self.folder.size])
            self.losetup()

            # Crypt the disk image
            p1 = subprocess.Popen(["echo", "\"" + self.folder.password + "\""], stdout=subprocess.PIPE)
            p2 = subprocess.Popen([CRYPTSETUP, "--batch-mode", "luksFormat", self.folder.loop], stdin=p1.stdout, stdout=subprocess.PIPE)
            p2.communicate()[0]
            #p2 = subprocess.check_call([CRYPTSETUP, "--batch-mode", "luksFormat", self.folder.loop])

            self.open_img()

            # Format the disk image
            subprocess.check_call([MKFS, self.mapper])

            self.close_img()
            self.delete_lo()



    def mount(self):
        """Mount an encrypted folder"""
        # if .crypt exists and contain a ref to ~/.crypt/XXX
        # this an unmounted crypted directory
        
        if self.folder.opened:
            raise AlreadyOpened()
            return
        self.open_img()
        # Mount
        subprocess.check_call([MOUNT, self.mapper, self.folder.path])
        self.folder.opened = True

    def unmount(self):
        """Unmount an encrypted folder"""
        # if .crypted exists, this a mounted crypted directory


        # Unmount
        subprocess.check_call([UMOUNT, mapper])

        self.close_img()
        self.delete_lo()
        self.folder.opened = False

    def uncrypt(self):
        """Uncrypt a folder"""
        tmp = os.path.join(TMPDIR, self.folder.digest)

        # Delete /tmp/cryptmanager/DIGEST if already exists
        Util().rm(tmp)

        self.mount()
        os.renames(self.folder.path, tmp)
        self.unmount()
        os.unlink(self.img)
        os.renames(tmp, self.folder.path)

    def losetup(self):
        """Set up the loop device"""
        # Get the first unused /dev/loopX
        p = os.popen (LOSETUP + " -f")
        for s in p:
            self.folder.loop = s.strip("\n")
        # Set up the loop device
        subprocess.check_call([LOSETUP, self.folder.loop, self.img])

    def open_img(self):
        """Open the disk image"""
        p1 = subprocess.Popen(["echo", "\"" + self.folder.password + "\""], \
            stdout=subprocess.PIPE)
        p2 = subprocess.Popen([CRYPTSETUP, "--batch-mode", "luksOpen", \
            self.folder.loop, self.folder.digest], stdin=p1.stdout, \
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        p2.communicate()
        if p2.returncode > 0:
            raise BadPassword()
        #subprocess.check_call([CRYPTSETUP, "luksOpen", self.folder.loop, \
        #self.folder.digest])

    def close_img(self):
        """Close the disk image"""
        subprocess.check_call([CRYPTSETUP, "luksClose", self.folder.digest])

    def delete_lo(self):
        """Delete the loop device"""
        subprocess.check_call([LOSETUP, "-d", self.folder.loop])
