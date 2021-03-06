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
# Foundation; either version 3 of the License, or (at your option) any later
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
import re
import time
import cPickle

# CRYPTDIR is the folder containing encrypted data.
# It is located at ~/.Crypt if in $HOME
# or /mount-point/.Crypt-user (like Trash).
MTAB = "/etc/mtab"
DEFAULT_CRYPTDIR = os.environ['HOME'] + "/.conceal/crypt"
CRYPTDIR = DEFAULT_CRYPTDIR
CACHE = os.environ['HOME'] + "/.conceal/cache"
TMPDIR ="/tmp/conceal"
FUSERMOUNT = "/usr/bin/fusermount"
ENCFS = "/usr/bin/encfs"
ENCFSCTL = "/usr/bin/encfsctl"
ECHO = "/bin/echo"
MOUNT = "/bin/mount"
# n for normal mode, p for paranoia mode
MODE = "p"

class AlreadyEncrypted(Exception):
    def __str__(self):
        return "This is already a crypted folder"


class BadPassword(Exception):
    def __str__(self):
        return "The password is wrong"


class NullPassword(Exception):
    def __str__(self):
        return "Password can not be null"


class AlreadyExists(Exception):
    def __str__(self):
        return "This folder already exists"


class AlreadyOpened(Exception):
    def __str__(self):
            return "This folder is already opened"


class NoEncrypted(Exception):
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
            return "This is not a folder"

#class NotDir(Exception):
#    def __str__(self):
#            return "Your not allowed to do this operation"

#class NotWritable(Exception):
#    def __str__(self):
#        return "This folder and all his files must be writable"
#


class UnexpectedError(Exception):
    def __str__(self):
        return "Unexpected error"


class Util:
    """Utilities"""
    
    def writable(self, path):
        """Test recursively if all the files in path are writable"""
        if path == os.environ['HOME']:
            return False
        if os.path.exists(path):
            for f in os.listdir(path):
                p = os.path.join(path, f)
                if os.path.isdir(p):
                    if not self.writable(p):
                        return False
                if os.path.isfile(p):
                    if not os.access(p, os.W_OK):
                        return False
            return True

    def rm(self, path):
        """Remove recursively a folder"""
        if os.path.exists(path):
            #for f in os.listdir(path):
            #    p = os.path.join(path, p)
            #    if os.path.isdir(p):
            #        self.rm(p)
            #        os.rmdir(p)
            #    if os.path.isfile(p):
            #        os.unlink(p)
            try:
                shutil.rmtree(path)
            except OSError:
                pass

    def fullpath(self, path):
        """Expand a path"""
        try:
            path = os.path.expanduser(path)
        except AttributeError:
            pass
        try:
            path = os.path.realpath(path)
        except AttributeError:
            pass
        try:
            path = os.path.normpath(path)
        except AttributeError:
            pass
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
    
    def mv(self, src, dst):
        """Move recursively"""
        if not os.path.exists(dst):
            os.makedirs(dst)
        for f in os.listdir(src):
            shutil.move(os.path.join(src, f), os.path.join(dst, f))

#    def mountpoint(self, path):
#        """Return the device mount point"""
#        if (os.path.ismount(path) or len(path) == 0):
#            return path
#        else:
#            return mountpoint(os.path.split(path)[0])


class Data:
    def __init__(self):
        if not os.path.exists(os.path.join(CACHE, "folders")):
            self.folders = Folders()
        else:
            f = open(os.path.join(CACHE, "folders"), "r")
            self.folders = cPickle.load(f)
            f.close()
        
    def save(self):
        if self.folders == None:
            return
        if not os.path.exists(CACHE):
            os.makedirs(CACHE)
        f = open(os.path.join(CACHE, "folders"), "w")
        cPickle.dump(self.folders, f, protocol = cPickle.HIGHEST_PROTOCOL)
        f.close()


class Folders:
    """Folders list"""
    def __init__(self):
        self.li = []
    
    def __getitem__(self, key):
        return self.li[key]

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

    def close_all(self):
        """Close all the open folders (i.e: before a reboot)"""
        self.clean()
        for f in self.li:
            if f.opened:
                Manage(f).unmount()
    
    def clean(self):
        """Delete unused Folders and empty TMPDIR"""
        for f in self.li:
            if not os.path.exists(CRYPTDIR + "/" + f.digest):
                self.li.remove(f)
            elif f.opened:
                encfs = Encfs(f)
                if not encfs.is_mounted():
                    f.opened = False


class Encfs:
    """Encfs wrapper"""
    def __init__(self, folder):
        self.folder = folder

    def change_password(self, old, new):
        """Change password"""
        p1 = subprocess.Popen([ECHO, "-e", old + "\n" + new + "\n"],\
            stdout=subprocess.PIPE)
        p2 = subprocess.Popen([ENCFSCTL, "autopasswd", self.folder.crypt],\
            stdin=p1.stdout, stdout=subprocess.PIPE)
        p2.communicate()[0]
        
        if p2.poll() is not 0:
            raise BadPassword()

    def encrypt(self, password):
        """Encrypt a folder"""
        print "Encrypting..."
        os.makedirs(self.folder.crypt)
        para = "\"%(mode)s\n%(pass)s\n\"" % {"mode": MODE, "pass": password}
        p1 = subprocess.Popen([ECHO, "-e", para], stdout=subprocess.PIPE)
        p2 = subprocess.Popen([ENCFS, "-S", self.folder.crypt,\
            self.folder.path], stdin=p1.stdout, stdout=subprocess.PIPE)
        p2.communicate()[0]
        if p2.poll() is not 0:
            raise BadPassword()

    def mount(self, password, idle=None):
        """Mount an encrypted folder"""
        print "Mounting..."
        if not os.path.exists(self.folder.path):
            os.makedirs(self.folder.path)
        p1 = subprocess.Popen([ECHO, password],\
            stdout=subprocess.PIPE)
        if idle == None:
            p2 = subprocess.Popen([ENCFS, "-S", self.folder.crypt,\
                self.folder.path, "--", "-o", "nonempty"], stdin=p1.stdout,\
                    stdout=subprocess.PIPE)
        else:
            p2 = subprocess.Popen([ENCFS, "-S", self.folder.crypt, "-i",\
                str(idle), self.folder.path, "--", "-o", "nonempty"],\
                    stdin=p1.stdout, stdout=subprocess.PIPE)
        p3 = p2.communicate()[0]
        if p2.poll() is not 0:
            raise BadPassword()

    def unmount(self):
        """Unmount an encrypted folder"""
        print "Unmounting..."
        subprocess.Popen([FUSERMOUNT, "-z", "-u", self.folder.path])
    
    def is_mounted(self):
        """Test if a folder is mounted"""
        p = subprocess.Popen([MOUNT], stdout=subprocess.PIPE)
        p = p.communicate()[0]
        p = p.split("\n")
        
        r = re.compile("^encfs on %s type fuse" % self.folder.path)
        for l in p:
            if r.match(l):
                return True
        return False

 
class Folder:
    """Folder information"""
    def __init__(self, path):
        self.path = Util().fullpath(path)
        if not os.path.isdir(self.path):
               raise NotDir()
               return
        self.digest = self.digest()
        self.crypt = os.path.join(CRYPTDIR, self.digest)
        self.opened = True
        self.attributes = {}
    
#    def cryptdir(self):
#        r = re.compile("^encfs on %s type fuse" % self.folder.path)
#        f = open(MTAB, "r")
#        for l in f:
#            if r.match(l):
#                return True
#        return False
        
    def __repr__(self):
        return repr(self.path)

    def digest(self):
        h = hashlib.sha256()
        h.update(self.path)
        return h.hexdigest()


class Manage:
    """Operations on a folder"""
    def __init__(self, folder):
        self.folder = folder
        self.encfs = Encfs(folder)

    def crypt(self, password):
        """Encrypt a folder"""
        # Create ~/.config/conceal if needed
        # The disk images are stored here
        if not os.path.exists(CRYPTDIR):
            os.makedirs(CRYPTDIR)
        
        # Test if the password is 7 characters long
        if len(password) == 0:
            raise NullPassword()
            return
             
        # Test if the disk images (sha256 hash of the path name) already exists
        if os.path.exists(self.folder.crypt):
            raise AlreadyEncrypted()
            return
            
#        if not Util().writable(self.folder.path):
#            raise NotWritable()
#            return

        tmp = os.path.join(TMPDIR, self.folder.digest)
        # Delete /tmp/conceal/DIGEST if already exists
        Util().rm(tmp)
        # Move the existing content in a tmp folder
        Util().mv(self.folder.path, tmp)
        # Create the mount point if needed
        
        
        # Crypt the disk image
        self.encfs.encrypt(password)
        self.folder.opened = True
        
        # Copy existing data in the crypted folder
        Util().mv(tmp, self.folder.path)

    def mount(self, password, idle=None):
        """Mount an encrypted folder"""
        
        if self.folder.opened:
            raise AlreadyOpened()
            return
        try:
            self.encfs.mount(password, idle)
        except BadPassword:
            raise BadPassword()
            return
        # Mount
        self.folder.opened = True
        
        return self.folder

    def unmount(self):
        """Unmount an encrypted folder"""
        if not self.folder.opened:
            raise NotOpened()
            return

        # Unmount
        self.encfs.unmount()
        self.folder.opened = False
        
        return self.folder

    def decrypt(self, password):
        """Decrypt a folder"""
        try:
            self.mount(password)
        except AlreadyOpened:
            self.unmount()
            self.decrypt(password)
            return
        except BadPassword:
            raise BadPassword()
            return
        tmp = os.path.join(TMPDIR, self.folder.digest)
        # Delete /tmp/conceal/DIGEST if already exists
        Util().rm(tmp)
        Util().mv(self.folder.path, tmp)
        self.unmount()
        Util().rm(self.folder.crypt)
        Util().mv(tmp, self.folder.path)
    
    def change_password(self, old, new):
        """Change a folder password"""
        
        try:
            self.encfs.change_password(old, new)
        except BadPassword:
            raise BadPassword()
