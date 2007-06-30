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

IMGDIR = os.environ['HOME'] + "/.config/cryptmanager"
DD = "/bin/dd"
LOSETUP = "/sbin/losetup"
CRYPTSETUP = "/sbin/cryptsetup"
MKFS = "/sbin/mkfs.ext3"
MOUNT = "/bin/mount"
UMOUNT = "/bin/umount"

class Folder:
	def __init__(self, path, passowrd, size, loop = None):
		"""Folder information"""
		self.path = path
		self.password = password
		self.size = size
		self.digest = digest()
		self.loop = loop

	def digest(self):
		return hashlib.sha256().new(self.path).hexdigest()

class Crypt:
	def __init__(self, folder):
		"""Encrypt a folder"""
		self.folder = folder
		create_img()

	def create_img(self):
		"""Create a disk image"""

		if not os.path.exists(IMGDIR):
			os.makedirs(IMGDIR)
		if not os.path.exists(self.folder.path):
			os.makedirs(self.folder.path)

		img = IMGDIR + "/" + self.folder.digest
		mapper = "/dev/mapper/" + self.folder.digest

		if os.path.exists(img):
			raise IMGexists, "This is already a crypted folder"
		else:
			subprocess.check_call([DD, "if=/dev/zero", "of=" + img, "bs=1M", "count=" + self.folder.size])
			p = os.popen (LOSETUP + " -f")
			for s in p:
				loop = s
			self.folder.loop = loop
			subprocess.check_call([LOSETUP, self.folder.loop, img])
			
			p1 = subprocess.Popen(["echo", "\"" + self.folder.password + "\""], stdout=PIPE)
			p2 = subprocess.Popen([CRYPTSETUP, "--batch-mode", "luksFormat", self.folder.loop], stdin=p1.stdout, stdout=PIPE)
			p2.communicate()[0]
			
			Mount(self.folder)

			subprocess.check_call([MKFS, mapper])
			subprocess.check_call([MOUNT, mapper, self.folder.path])

class Mount:
	def __init__(self, folder):
		"""Mount an encrypted folder"""
		# if .crypt exists and contain a ref to ~/.crypt/XXX this an unmounted crypted driectory
		self.folder = folder

		p1 = subprocess.Popen(["echo", "\"" + self.folder.password + "\""], stdout=PIPE)
		p2 = subprocess.Popen([CRYPTSETUP, "--batch-mode", "lukOpen", self.folder.loop, self.folder.digest], stdin=p1.stdout, stdout=PIPE)
		p2.communicate()[0]

class Unmount:
	def __init__(self, d):
		"""Unmount an encrypted folder"""
		# if .crypted exists, this a mounted crypted directory
		mapper = "/dev/mapper/" + self.folder.digest

		subprocess.check_call([UMOUNT, mapper])
		subprocess.check_call([CRYPTSETUP, "luksClose", self.folder.digest])
		subprocess.check_call([LOSETUP, "-d", self.folder.loop])
