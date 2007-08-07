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

import nautilus
import urllib
import gettext
import locale
import conceal
import subprocess
import os

import __builtin__
__builtin__._ = gettext.gettext

# Crypt Manager extension for nautilus
EMBLEM = "readonly"

class concealExtension(nautilus.InfoProvider, nautilus.MenuProvider):
    def __init__(self):
        pass

    def _load_data(self):
        data = conceal.Data()
        self.folders = data.folders
        self.folders.clean()
     
    def _clicked(self, menu, file):
        if self.status == 1:
            p = subprocess.Popen(["conceal-gtk", "--crypt", self.filename])
            if p.poll() == 0:
                file.add_emblem(EMBLEM)
        if self.status == 2:
            p = subprocess.Popen(["conceal-gtk", "--close", self.filename])
        if self.status == 3:
            p = subprocess.Popen(["conceal-gtk", "--open", self.filename])

    def _get_status(self):
        try:
            folder = self.folders.get(self.filename)
        except conceal.NoEncrypted:
            self.status = 1
        else:
            if folder.opened:
                self.status = 2
            else:
                self.status = 3

    def _get_messages(self):
        """1: unencrypted, 2: opened, 3: closed"""
        if self.status == 1:
            self.entry = _("Encrypt")
            self.desc = _("Encrypt this folder using Crypt Manager")
        elif self.status == 2:
            self.entry = _("Close")
            self.desc = _("Close this encrypted folder")
        else:
            self.entry = _("Open")
            self.desc = _("Open this encrypted folder")

    def update_file_info(self, file):
        self.filename = urllib.unquote(file.get_uri()[7:])
        f = self.filename.split("/")[-1]
        if not file.is_directory():
            # Workaround to ask the password
            # when entering in an encrypted folder
            if f == "conceal.lock":
                parent = urllib.unquote(file.get_parent_uri()[7:])
                os.unlink(self.filename)
                p = subprocess.Popen(["conceal-gtk", "--open",
                    parent])
            return
        self._load_data()
        self._get_status()

        if self.status == 3 and not os.path.exists(os.path.join(self.filename,
            "conceal.lock")):
            f = open (os.path.join(self.filename, "conceal.lock"), "w")
            f.write("")
            f.close()

        if self.status == 2 or self.status == 3:
            file.add_emblem(EMBLEM)

    def get_file_items(self, window, files):
        self._load_data()
        if len(files) != 1:
            return

        file = files[0]
        if not file.is_directory():
            return
        self.filename = urllib.unquote(file.get_uri()[7:]) 
        
        self._get_status()
        self._get_messages()

        
        menu = nautilus.MenuItem(
            "NautilusPython::concealExtension",
            self.entry,
            self.desc
        )
        menu.connect("activate", self._clicked, file)
        return menu,
         
    def get_background_items(self, window, file):
        return
