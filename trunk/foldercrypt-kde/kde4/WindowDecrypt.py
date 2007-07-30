# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt4/WindowDecrypt.ui'
#
# Created: Mon Jul 30 20:29:49 2007
#      by: PyQt4 UI code generator 4.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_WindowDecrypt(object):
    def setupUi(self, WindowDecrypt):
        WindowDecrypt.setObjectName("WindowDecrypt")
        WindowDecrypt.resize(QtCore.QSize(QtCore.QRect(0,0,283,132).size()).expandedTo(WindowDecrypt.minimumSizeHint()))
        WindowDecrypt.setSizeGripEnabled(True)

        self.decrypt_password2 = QtGui.QLabel(WindowDecrypt)
        self.decrypt_password2.setGeometry(QtCore.QRect(30,60,70,20))
        self.decrypt_password2.setWordWrap(False)
        self.decrypt_password2.setObjectName("decrypt_password2")

        self.Layout1 = QtGui.QWidget(WindowDecrypt)
        self.Layout1.setGeometry(QtCore.QRect(20,90,250,33))
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

        self.decrypt_ok = QtGui.QPushButton(self.Layout1)
        self.decrypt_ok.setAutoDefault(True)
        self.decrypt_ok.setDefault(True)
        self.decrypt_ok.setObjectName("decrypt_ok")
        self.hboxlayout.addWidget(self.decrypt_ok)

        self.decrypt_cancel = QtGui.QPushButton(self.Layout1)
        self.decrypt_cancel.setAutoDefault(True)
        self.decrypt_cancel.setObjectName("decrypt_cancel")
        self.hboxlayout.addWidget(self.decrypt_cancel)

        self.decrypt_path = QtGui.QLabel(WindowDecrypt)
        self.decrypt_path.setGeometry(QtCore.QRect(30,30,60,20))
        self.decrypt_path.setWordWrap(False)
        self.decrypt_path.setObjectName("decrypt_path")

        self.textLabel2 = QtGui.QLabel(WindowDecrypt)
        self.textLabel2.setGeometry(QtCore.QRect(110,30,150,21))
        self.textLabel2.setWordWrap(False)
        self.textLabel2.setObjectName("textLabel2")

        self.decrypt_password = QtGui.QLineEdit(WindowDecrypt)
        self.decrypt_password.setGeometry(QtCore.QRect(110,60,150,22))
        self.decrypt_password.setEchoMode(QtGui.QLineEdit.Password)
        self.decrypt_password.setObjectName("decrypt_password")

        self.retranslateUi(WindowDecrypt)
        QtCore.QObject.connect(self.decrypt_ok,QtCore.SIGNAL("clicked()"),WindowDecrypt.accept)
        QtCore.QObject.connect(self.decrypt_cancel,QtCore.SIGNAL("clicked()"),WindowDecrypt.reject)
        QtCore.QMetaObject.connectSlotsByName(WindowDecrypt)
        WindowDecrypt.setTabOrder(self.decrypt_password,self.decrypt_ok)
        WindowDecrypt.setTabOrder(self.decrypt_ok,self.decrypt_cancel)

    def retranslateUi(self, WindowDecrypt):
        WindowDecrypt.setWindowTitle(QtGui.QApplication.translate("WindowDecrypt", "Decrypt", None, QtGui.QApplication.UnicodeUTF8))
        self.decrypt_password2.setText(QtGui.QApplication.translate("WindowDecrypt", "Password:", None, QtGui.QApplication.UnicodeUTF8))
        self.decrypt_ok.setText(QtGui.QApplication.translate("WindowDecrypt", "&OK", None, QtGui.QApplication.UnicodeUTF8))
        self.decrypt_cancel.setText(QtGui.QApplication.translate("WindowDecrypt", "&Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.decrypt_path.setText(QtGui.QApplication.translate("WindowDecrypt", "Path:", None, QtGui.QApplication.UnicodeUTF8))

