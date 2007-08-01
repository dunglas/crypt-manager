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

import os
import sys
import gettext
import locale
from qt import *
from kdeui import KCModule
from kdecore import KApplication, KCmdLineArgs, KAboutData
from kfile import KDirSelectDialog
from ui.WindowManager import *
from ui.WindowOpen import *
from ui.WindowCrypt import *
from ui.WindowProperties import *
from ui.WindowDecrypt import *
from ui.WindowError import *
import foldercrypt

import __builtin__
__builtin__._ = gettext.gettext

APPNAME="foldercrypt-kde"
APPVERSION="0.1"
CACHE = os.environ['HOME'] + "/.foldercrypt/cache"
ICON = "/usr/share/foldercrypt/icon.png"
wlist = []

# Are we running as a separate standalone application or in KControl?
standalone = __name__=='__main__'

if standalone:
    programbase = QMainWindow
else:
    programbase = KCModule

class Util:
    """Utilities"""
    def error_box(self, msg):
        """Display an error box"""
        self.win = WindowError()
        self.win.show()
        wlist.append(self.win)
        
        self.win.error_msg.setText(msg)
        app.connect(self.win.error_ok, SIGNAL("clicked()"), self.win,\
            SLOT("close()"))
        app.connect(app, SIGNAL("lastWindowClosed()"), app,\
            SLOT("quit()"))
    
    def valid_properties(self, new, confirmation):
        """Validation for the crypt window"""
        if len(new) == 0:
            self.error_box(_("Password can not be null."))
            return False
        if not new == confirmation:
            self.error_box(
                _("New password do not match with the confirmation."))
            return False
        return True


class Manager(programbase):
    def __init__(self):
        programbase.__init__(self, None, None)
        self.win = WindowManager()
        self.win.show()
        wlist.append(self.win)

        #self.win.manager_open_close.setEnabled(False)

        app.connect(self.win.manager_crypt, SIGNAL("clicked()"), Crypt)
        app.connect(self.win.manager_decrypt, SIGNAL("clicked()"), Decrypt)
        app.connect(self.win.manager_open_close, SIGNAL("clicked()"),\
            self.open_close)
        app.connect(self.win.manager_properties, SIGNAL("clicked()"),\
            Properties)
        app.connect(self.win.manager_reset, SIGNAL("clicked()"), self.test)
        app.connect(self.win.manager_apply, SIGNAL("clicked()"), self.test)
        app.connect(app, SIGNAL("lastWindowClosed()"), app,\
            SLOT("quit()"))
        app.connect(self.win.manager_list, SIGNAL("selectionChanged()"),\
            self.select)
        
        self.update()
    
    def select(self):
        selected = False
        item = self.win.manager_list.firstChild()
        while item:
            if item.isSelected ():
                selected = True
                self.path = item.text(1)
                if item.text(2) == _("Yes"):
                    self.win.manager_open_close.setText(_("Close"))
                else:
                    self.win.manager_open_close.setText(_("Open"))
                item = False
            else:
                item = item.nextSibling ()
        self.win.manager_open_close.setEnabled(selected)
        self.win.manager_properties.setEnabled(selected)
        self.win.manager_decrypt.setEnabled(selected)
    
    def open_close(self):
        if self.win.manager_open_close.text() == "&" + _("Open"):
            Open()
        else:
            Close()
    
    def test(self):
        print self.win.manager_list.takeItem(\
            self.win.manager_list.currentItem())
    
    def update(self):
        """Update the folders list"""
        self.win.manager_list.clear()
        for f in folders.li:
            #path = f.path.split("/")
            #path = path[len(path) - 1]
            if f.opened == True:
                o = _("Yes")
            else:
                o = _("No")
            self.win.manager_list.insertItem(QListViewItem(\
                self.win.manager_list, "", f.path, o))


class Open:
    def __init__(self, path = None):     
        self.win = WindowOpen()
        self.win.show()
        wlist.append(self.win)
        
        if path == None:
            path = manager.path
        self.win.open_path.setText(path)
        
        global this
        this = self
        
        app.connect(self.win.open_close, SIGNAL("stateChanged(int)"),\
            this.time)
        app.connect(self.win.open_ok, SIGNAL("clicked()"), this.run)
        app.connect(self.win.open_cancel, SIGNAL("clicked()"), self.win,\
            SLOT("close()"))
        app.connect(app, SIGNAL("lastWindowClosed()"), app,\
            SLOT("quit()"))
        
    def time(self):
        if self.win.open_close.state() == 2:
            self.win.open_time.setEnabled(True)
        else:
            self.win.open_time.setEnabled(False)

    def run(self):
        if self.win.open_close.state() == 2:
            idle = self.win.open_time.value()
        else:
            idle = None

        path = str(self.win.open_path.text())
        password = str(self.win.open_password.text())
        
        try:
            folder = folders.get(path)
        except foldercrypt.NoEncrypted:
            Util().error_box(_("%s is not a crypted directory.") % folder.path)
            return
        try:
            folder = foldercrypt.Manage(folder).mount(password, idle)
        except foldercrypt.AlreadyOpened:
            Util().error_box(_("%s is already open.") % folder.path)
        except foldercrypt.BadPassword:
            Util().error_box(_("Your password is wrong."))
        else:
            folders.update(folder)
            manager.update()
            self.win.close()


class Close:
    def __init__(self, path = None):
        if path == None:
            path = str(manager.path)
        try:
            folder = folders.get(path)
        except foldercrypt.NoEncrypted:
            Util().error_box(_("%s is not a crypted directory.") % folder.path)
        try:
            folder = foldercrypt.Manage(folder).unmount()
        except foldercrypt.NotOpened:
            Util().error_box(_("%s is not opened.") % folder.path)
        else:
            folders.update(folder)
            try:
                manager.update()
            except:
                pass

class Crypt:
    def __init__(self):
        self.win = WindowCrypt()
        self.win.show()
        wlist.append(self.win)
        
        global this_crypt
        this_crypt = self
        
        app.connect(self.win.crypt_file, SIGNAL("clicked()"),\
            this_crypt.choose)
        app.connect(self.win.crypt_ok, SIGNAL("clicked()"), this_crypt.crypt)
        app.connect(this_crypt.win.crypt_cancel, SIGNAL("clicked()"),\
            self.win, SLOT("close()"))
        app.connect(app, SIGNAL("lastWindowClosed()"), app,\
            SLOT("quit()"))
        
    def crypt(self):
        if self.valid():
            self.run()

    def valid(self):
        """Validation for the crypt window"""
        self.path = foldercrypt.Util().fullpath(str(self.win.crypt_path.text()))
        self.password = str(self.win.crypt_password.text())
        self.confirmation = str(self.win.crypt_confirmation.text())
        self.win.crypt_path.setText(self.path)
        if not os.path.exists(self.path):
            Util().error_box(_("You must select a valid folder."))
            return False
        if len(self.password) == 0:
            Util().error_box(_("Password can not be null."))
            return False
        if not self.password == self.confirmation:
            Util().error_box(_("Password do not match with the confirmation."))
            return False
        return True

    def choose(self):
        path = KDirSelectDialog.selectDirectory(QString.null, 1).path()
        self.win.crypt_path.setText(path)

    def run(self):
        """Main"""
        self.folder = foldercrypt.Folder(self.path)
        try:
            foldercrypt.Manage(self.folder).\
                crypt(self.password)
        except foldercrypt.AlreadyEncrypted:
            Util().error_box(_("%s is already an encrypted folder.")
                % self.folder.path)
        except foldercrypt.NotWritable:
            Util().error_box(
                _("%s and all his files must be writable.") % self.folder.path)
        else:
            folders.add(self.folder)
            self.win.close()
            manager.update()

class Test:
    def __init__(self):
        print "hahah"

class Decrypt:
    def __init__(self, path = None):
        self.win = WindowDecrypt()
        self.win.show()
        wlist.append(self.win)
        
        if path == None:
            self.path = manager.path
        else:
            self.path = path
        self.win.decrypt_path.setText(self.path)
        
        global this
        this = self
        
        app.connect(self.win.decrypt_ok, SIGNAL("clicked()"), this.decrypt)
        app.connect(self.win.decrypt_cancel, SIGNAL("clicked()"), self.win,\
            SLOT("close()"))
        app.connect(app, SIGNAL("lastWindowClosed()"), app,\
            SLOT("quit()"))

    def decrypt(self):
        password = str(self.win.decrypt_password.text())
        try:
            folder = folders.get(self.path)
        except foldercrypt.AlreadyOpened:
            Util().error_box(_("%s is already open.") % folder.path)  
        try:
            foldercrypt.Manage(folder).decrypt(password)
        except foldercrypt.BadPassword:
            Util().error_box(_("Your password is wrong."))
        else:
            folders.rem(folder)
            self.win.close()


class Properties:
    def __init__(self, path = None):
        self.win = WindowProperties()
        self.win.show()
        wlist.append(self.win)
        
        if path == None:
            self.path = manager.path
        else:
            self.path = path
        self.win.properties_path.setText(self.path)
        
        global this
        this = self
        
        app.connect(self.win.properties_ok, SIGNAL("clicked()"),\
            this.run)
        app.connect(self.win.properties_cancel, SIGNAL("clicked()"),\
            self.win, SLOT("close()"))
        app.connect(app, SIGNAL("lastWindowClosed()"), app,\
            SLOT("quit()"))

    def valid(self):
        """Validation for the crypt window"""
        self.new = str(self.win.properties_new.text())
        self.confirm = str(self.win.properties_confirm.text())
        self.old = str(self.win.properties_old.text())
        if len(self.new) == 0:
            self.error_box(_("Password can not be null."))
            return False
        if not self.new == self.confirm:
            self.error_box(
                _("New password do not match with the confirmation."))
            return False
        return True
    
    def run(self):
        if self.valid():
            try:
                folder = folders.get(self.path)
            except foldercrypt.NoEncrypted:
                Util().error_box(_("%s is not a crypted directory.")\
                    % folder.path)
            try:
                folder = foldercrypt.Manage(folder).change_password(self.old,\
                    self.new)
            except foldercrypt.BadPassword:
                Util().error_box(_("Bad password."))
            else:
                self.win.close()
    
    
def exit(para=0):
    data.save()

def start():
    global data
    global folders
    data = foldercrypt.Data()
    folders = data.folders
    folders.clean()

def about_data():
    about = KAboutData("foldercrypt-kde", APPNAME, APPVERSION,\
        "Encrypted folder manager", KAboutData.License_GPL,\
        "Copyright (C) 2007 Kévin Dunglas",\
        "Part of the Google SoC 2007. Mentored by Jani Monoses.")
    return about

def create_serviceconfig(parent, name):
    print "hahaa"
    global app
    start()
    app = KApplication()
    return SysVInitApp(parent, name)


if standalone:
    global app
    global manager
    start()
    app = KApplication(sys.argv, "Foldercrypt")
    manager = Manager()
    app.exec_loop()

exit()
