# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt4/WindowCrypt.ui'
#
# Created: Mon Jul 30 20:29:25 2007
#      by: PyQt4 UI code generator 4.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_WindowCrypt(object):
    def setupUi(self, WindowCrypt):
        WindowCrypt.setObjectName("WindowCrypt")
        WindowCrypt.resize(QtCore.QSize(QtCore.QRect(0,0,306,164).size()).expandedTo(WindowCrypt.minimumSizeHint()))

        self.textLabel1_2 = QtGui.QLabel(WindowCrypt)
        self.textLabel1_2.setGeometry(QtCore.QRect(10,50,91,21))
        self.textLabel1_2.setWordWrap(False)
        self.textLabel1_2.setObjectName("textLabel1_2")

        self.textLabel1_2_2 = QtGui.QLabel(WindowCrypt)
        self.textLabel1_2_2.setGeometry(QtCore.QRect(10,80,91,21))
        self.textLabel1_2_2.setWordWrap(False)
        self.textLabel1_2_2.setObjectName("textLabel1_2_2")

        self.textLabel1 = QtGui.QLabel(WindowCrypt)
        self.textLabel1.setGeometry(QtCore.QRect(10,20,91,21))
        self.textLabel1.setWordWrap(False)
        self.textLabel1.setObjectName("textLabel1")

        self.Layout1 = QtGui.QWidget(WindowCrypt)
        self.Layout1.setGeometry(QtCore.QRect(0,120,300,33))
        self.Layout1.setObjectName("Layout1")

        self.hboxlayout = QtGui.QHBoxLayout(self.Layout1)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setLeftMargin(0)
        self.hboxlayout.setTopMargin(0)
        self.hboxlayout.setRightMargin(0)
        self.hboxlayout.setBottomMargin(0)
        self.hboxlayout.setObjectName("hboxlayout")

        spacerItem = QtGui.QSpacerItem(20,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)

        self.crypt_ok = QtGui.QPushButton(self.Layout1)
        self.crypt_ok.setAutoDefault(True)
        self.crypt_ok.setDefault(True)
        self.crypt_ok.setObjectName("crypt_ok")
        self.hboxlayout.addWidget(self.crypt_ok)

        self.crypt_cancel = QtGui.QPushButton(self.Layout1)
        self.crypt_cancel.setAutoDefault(True)
        self.crypt_cancel.setObjectName("crypt_cancel")
        self.hboxlayout.addWidget(self.crypt_cancel)

        self.crypt_confirmation = QtGui.QLineEdit(WindowCrypt)
        self.crypt_confirmation.setGeometry(QtCore.QRect(110,80,190,21))
        self.crypt_confirmation.setEchoMode(QtGui.QLineEdit.Password)
        self.crypt_confirmation.setObjectName("crypt_confirmation")

        self.crypt_password = QtGui.QLineEdit(WindowCrypt)
        self.crypt_password.setGeometry(QtCore.QRect(110,50,190,21))
        self.crypt_password.setEchoMode(QtGui.QLineEdit.Password)
        self.crypt_password.setObjectName("crypt_password")

        self.crypt_path = QtGui.QLineEdit(WindowCrypt)
        self.crypt_path.setGeometry(QtCore.QRect(111,20,190,21))
        self.crypt_path.setEchoMode(QtGui.QLineEdit.Password)
        self.crypt_path.setObjectName("crypt_path")

        self.retranslateUi(WindowCrypt)
        QtCore.QMetaObject.connectSlotsByName(WindowCrypt)
        WindowCrypt.setTabOrder(self.crypt_path,self.crypt_password)
        WindowCrypt.setTabOrder(self.crypt_password,self.crypt_confirmation)
        WindowCrypt.setTabOrder(self.crypt_confirmation,self.crypt_ok)
        WindowCrypt.setTabOrder(self.crypt_ok,self.crypt_cancel)

    def retranslateUi(self, WindowCrypt):
        WindowCrypt.setWindowTitle(QtGui.QApplication.translate("WindowCrypt", "Encrypt", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1_2.setText(QtGui.QApplication.translate("WindowCrypt", "Password:", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1_2_2.setText(QtGui.QApplication.translate("WindowCrypt", "Confirmation:", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1.setText(QtGui.QApplication.translate("WindowCrypt", "Path:", None, QtGui.QApplication.UnicodeUTF8))
        self.crypt_ok.setText(QtGui.QApplication.translate("WindowCrypt", "&OK", None, QtGui.QApplication.UnicodeUTF8))
        self.crypt_cancel.setText(QtGui.QApplication.translate("WindowCrypt", "&Cancel", None, QtGui.QApplication.UnicodeUTF8))

