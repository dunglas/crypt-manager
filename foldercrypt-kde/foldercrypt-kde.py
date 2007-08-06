#!/usr/bin/python
# -*- coding: UTF-8 -*-
###########################################################################
# serviceconfig.py - description                                          #
# ------------------------------                                          #
# begin     : Wed Apr 30 2003                                             #
# copyright : (C) 2003-2006 by Simon Edwards                              #
# email     : simon@simonzone.com                                         #
#                                                                         #
###########################################################################
#                                                                         #
#   This program is free software; you can redistribute it and/or modify  #
#   it under the terms of the GNU General Public License as published by  #
#   the Free Software Foundation; either version 2 of the License, or     #
#   (at your option) any later version.                                   #
#                                                                         #
###########################################################################


import os
import sys
import gettext
import locale
from qt import *
from qt import *
from kdeui import *
from kdecore import *
from kfile import KDirSelectDialog
import foldercrypt
from ui.WindowOpen import *
from ui.WindowCrypt import *
from ui.WindowProperties import *
from ui.WindowDecrypt import *
from ui.WindowError import *

import __builtin__
__builtin__._ = gettext.gettext

APPNAME="foldercrypt-kde"
APPVERSION="0.0.2"
CACHE = os.environ['HOME'] + "/.foldercrypt/cache"
ICON = "/usr/share/foldercrypt/icon.png"
wlist = []


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


# Are we running as a separate standalone application or in KControl?
standalone = __name__=='__main__'


# Try translating this code to C++. I dare ya!
if standalone:
    programbase = KDialogBase
else:
    programbase = KCModule

# is_shown exists to prevent loadDescriptions from running two times, which is 
# the case when we're running inside kcontrol. Yes, this is an ugly hack. :(
# It's set to True after show has finished once. It doesn't play a role when
# we're running standalone.
is_shown = False

class Manager(programbase):
    def __init__(self, parent=None, name=None):
        global standalone, manager
        manager = self

        if standalone:
            KDialogBase.__init__(self,KJanusWidget.Plain,"Foldercrypt", \
                KDialogBase.User1|KDialogBase.Close, KDialogBase.Close)
            self.setButtonText(KDialogBase.User1,i18n("About"))
        else:
            KCModule.__init__(self,parent,name)
            self.setButtons(1)
            self.aboutdata = MakeAboutData()

        self.updatingGUI = False

        if standalone:
            toplayout = QVBoxLayout( self.plainPage(), 0, KDialog.spacingHint() )
            tophb = QSplitter(Qt.Horizontal, self.plainPage())
        else:
            toplayout = QVBoxLayout( self, 0, KDialog.spacingHint() )
            tophb = QSplitter(Qt.Horizontal, self)
        
        self.manager_crypt = QPushButton(self,"manager_crypt")
        self.manager_crypt.setGeometry(QRect(490,30,90,30))

        self.manager_properties = QPushButton(self,"manager_properties")
        self.manager_properties.setEnabled(0)
        self.manager_properties.setGeometry(QRect(490,110,90,30))

        self.manager_decrypt = QPushButton(self,"manager_decrypt")
        self.manager_decrypt.setEnabled(0)
        self.manager_decrypt.setGeometry(QRect(490,150,90,30))

        self.manager_list = QListView(self,"manager_list")
        self.manager_list.addColumn(QString.null)
        self.manager_list.addColumn(_("Path"))
        self.manager_list.addColumn(_("Open"))
        self.manager_list.setGeometry(QRect(30,30,450,360))
        self.manager_list.setAllColumnsShowFocus(0)

        self.manager_open_close = QPushButton(self,"manager_open_close")
        self.manager_open_close.setEnabled(0)
        self.manager_open_close.setGeometry(QRect(490,70,90,30))
        
        self.setTabOrder(self.manager_list,self.manager_crypt)
        self.setTabOrder(self.manager_crypt,self.manager_open_close)
        self.setTabOrder(self.manager_open_close,self.manager_properties)
        self.setTabOrder(self.manager_properties,self.manager_decrypt)

        self.setCaption(_("Manager"))
        self.manager_crypt.setText(_("Encrypt"))
        self.manager_properties.setText(_("Properties"))
        self.manager_decrypt.setText(_("Decrypt"))
        self.manager_list.header().setLabel(0," ")
        self.manager_list.header().setLabel(1,_("Path"))
        self.manager_list.header().setLabel(2,_("Open"))
        self.manager_open_close.setText(_("Open"))
        
        self.resize(QSize(621,480))
        
        app.connect(self.manager_crypt, SIGNAL("clicked()"), Crypt)
        app.connect(self.manager_decrypt, SIGNAL("clicked()"), Decrypt)
        app.connect(self.manager_open_close, SIGNAL("clicked()"),\
            self.open_close)
        app.connect(self.manager_properties, SIGNAL("clicked()"),\
            Properties)
        app.connect(app, SIGNAL("lastWindowClosed()"), app,\
            SLOT("quit()"))
        app.connect(self.manager_list, SIGNAL("selectionChanged()"),\
            self.select)
        
        self.update()

    def select(self):
        selected = False
        item = self.manager_list.firstChild()
        while item:
            if item.isSelected ():
                selected = True
                self.path = item.text(1)
                if item.text(2) == _("Yes"):
                    self.manager_open_close.setText(_("Close"))
                else:
                    self.manager_open_close.setText(_("Open"))
                item = False
            else:
                item = item.nextSibling ()
        self.manager_open_close.setEnabled(selected)
        self.manager_properties.setEnabled(selected)
        self.manager_decrypt.setEnabled(selected)
    
    def open_close(self):
        print self.manager_open_close.text()
        if self.manager_open_close.text() == "&" + _("Open"):
            Open()
        else:
            Close()
    
    def test(self):
        print self.manager_list.takeItem(\
            self.manager_list.currentItem())
    
    def update(self):
        """Update the folders list"""
        self.manager_list.clear()
        for f in folders.li:
            #path = f.path.split("/")
            #path = path[len(path) - 1]
            if f.opened == True:
                o = _("Yes")
            else:
                o = _("No")
            self.manager_list.insertItem(QListViewItem(\
                self.manager_list, "", f.path, o))


    # KDialogBase method
    def exec_loop(self):
        global programbase

        programbase.exec_loop(self)


    def __selectFirstService(self):                
        pass

    def show(self):
        global standalone
        programbase.show(self)

    # KControl virtual void methods
    def load(self):
        pass
    def save(self):
        pass
    def defaults(self):
        pass        
    def sysdefaults(self):
        pass

    def aboutData(self):
        # Return the KAboutData object which we created during initialisation.
        return self.aboutdata

    def buttons(self):
        # Only supply a Help button. Other choices are Default and Apply.
        return KCModule.Help

    def run(self,argslist):
        self.exec_loop()

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
        except foldercrypt.foldercrypt.NoEncrypted:
            Util().error_box(_("%s is not an encrypted directory.") % self.path)   
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

# Factory function for KControl
def create_foldercrypt(parent,name):
    global app
    app = KApplication.kApplication()
    return Manager(parent, name)

def MakeAboutData():
    aboutdata = KAboutData("foldercrypt-kde", APPNAME, APPVERSION,\
        "Encrypted folder manager", KAboutData.License_GPL,\
        "Copyright (C) 2007 Kévin Dunglas",\
        "Part of the Google SoC 2007. Mentored by Jani Monoses.")
    return aboutdata

data = foldercrypt.Data()
folders = data.folders
folders.clean()

if standalone:
    aboutdata = MakeAboutData()
    KCmdLineArgs.init(sys.argv,aboutdata)

    app = KApplication()
    manager = Manager()
    manager.exec_loop()

exit()
