# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt4/WindowManager.ui'
#
# Created: Mon Jul 30 20:37:44 2007
#      by: PyQt4 UI code generator 4.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_WindowManager(object):
    def setupUi(self, WindowManager):
        WindowManager.setObjectName("WindowManager")
        WindowManager.resize(QtCore.QSize(QtCore.QRect(0,0,557,414).size()).expandedTo(WindowManager.minimumSizeHint()))

        self.widget = QtGui.QWidget(WindowManager)
        self.widget.setGeometry(QtCore.QRect(0,0,557,414))
        self.widget.setObjectName("widget")

        self.manager_reset = QtGui.QPushButton(self.widget)
        self.manager_reset.setGeometry(QtCore.QRect(360,380,90,30))
        self.manager_reset.setObjectName("manager_reset")

        self.manager_apply = QtGui.QPushButton(self.widget)
        self.manager_apply.setGeometry(QtCore.QRect(460,380,90,30))
        self.manager_apply.setObjectName("manager_apply")

        self.manager_crypt = QtGui.QPushButton(self.widget)
        self.manager_crypt.setGeometry(QtCore.QRect(460,10,90,30))
        self.manager_crypt.setObjectName("manager_crypt")

        self.manager_properties = QtGui.QPushButton(self.widget)
        self.manager_properties.setEnabled(False)
        self.manager_properties.setGeometry(QtCore.QRect(460,70,90,30))
        self.manager_properties.setObjectName("manager_properties")

        self.manager_decrypt = QtGui.QPushButton(self.widget)
        self.manager_decrypt.setEnabled(False)
        self.manager_decrypt.setGeometry(QtCore.QRect(460,100,90,30))
        self.manager_decrypt.setObjectName("manager_decrypt")

        self.manager_open_close = QtGui.QPushButton(self.widget)
        self.manager_open_close.setEnabled(False)
        self.manager_open_close.setGeometry(QtCore.QRect(460,40,90,30))
        self.manager_open_close.setObjectName("manager_open_close")

        self.manager_list = QtGui.QTreeView(self.widget)
        self.manager_list.setGeometry(QtCore.QRect(10,10,441,361))
        self.manager_list.setObjectName("manager_list")
        WindowManager.setCentralWidget(self.widget)

        self.retranslateUi(WindowManager)
        QtCore.QMetaObject.connectSlotsByName(WindowManager)
        WindowManager.setTabOrder(self.manager_list,self.manager_crypt)
        WindowManager.setTabOrder(self.manager_crypt,self.manager_open_close)
        WindowManager.setTabOrder(self.manager_open_close,self.manager_properties)
        WindowManager.setTabOrder(self.manager_properties,self.manager_decrypt)
        WindowManager.setTabOrder(self.manager_decrypt,self.manager_reset)
        WindowManager.setTabOrder(self.manager_reset,self.manager_apply)

    def retranslateUi(self, WindowManager):
        WindowManager.setWindowTitle(QtGui.QApplication.translate("WindowManager", "Manager", None, QtGui.QApplication.UnicodeUTF8))
        self.manager_reset.setText(QtGui.QApplication.translate("WindowManager", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.manager_apply.setText(QtGui.QApplication.translate("WindowManager", "Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.manager_crypt.setText(QtGui.QApplication.translate("WindowManager", "Encrypt", None, QtGui.QApplication.UnicodeUTF8))
        self.manager_properties.setText(QtGui.QApplication.translate("WindowManager", "Properties", None, QtGui.QApplication.UnicodeUTF8))
        self.manager_decrypt.setText(QtGui.QApplication.translate("WindowManager", "Decrypt", None, QtGui.QApplication.UnicodeUTF8))
        self.manager_open_close.setText(QtGui.QApplication.translate("WindowManager", "Open", None, QtGui.QApplication.UnicodeUTF8))

