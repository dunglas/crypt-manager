# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt4/WindowOpen.ui'
#
# Created: Mon Jul 30 20:29:41 2007
#      by: PyQt4 UI code generator 4.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_WindowOpen(object):
    def setupUi(self, WindowOpen):
        WindowOpen.setObjectName("WindowOpen")
        WindowOpen.resize(QtCore.QSize(QtCore.QRect(0,0,324,188).size()).expandedTo(WindowOpen.minimumSizeHint()))
        WindowOpen.setSizeGripEnabled(True)

        self.Layout1 = QtGui.QWidget(WindowOpen)
        self.Layout1.setGeometry(QtCore.QRect(10,130,300,33))
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

        self.open_ok = QtGui.QPushButton(self.Layout1)
        self.open_ok.setAutoDefault(True)
        self.open_ok.setDefault(True)
        self.open_ok.setObjectName("open_ok")
        self.hboxlayout.addWidget(self.open_ok)

        self.open_cancel = QtGui.QPushButton(self.Layout1)
        self.open_cancel.setAutoDefault(True)
        self.open_cancel.setObjectName("open_cancel")
        self.hboxlayout.addWidget(self.open_cancel)

        self.textLabel1_2 = QtGui.QLabel(WindowOpen)
        self.textLabel1_2.setGeometry(QtCore.QRect(10,60,91,21))
        self.textLabel1_2.setWordWrap(False)
        self.textLabel1_2.setObjectName("textLabel1_2")

        self.textLabel1_2_2 = QtGui.QLabel(WindowOpen)
        self.textLabel1_2_2.setGeometry(QtCore.QRect(10,20,91,21))
        self.textLabel1_2_2.setWordWrap(False)
        self.textLabel1_2_2.setObjectName("textLabel1_2_2")

        self.textLabel3 = QtGui.QLabel(WindowOpen)
        self.textLabel3.setGeometry(QtCore.QRect(200,100,110,21))
        self.textLabel3.setWordWrap(False)
        self.textLabel3.setObjectName("textLabel3")

        self.open_close = QtGui.QCheckBox(WindowOpen)
        self.open_close.setGeometry(QtCore.QRect(10,100,130,21))
        self.open_close.setObjectName("open_close")

        self.open_time = QtGui.QSpinBox(WindowOpen)
        self.open_time.setEnabled(False)
        self.open_time.setGeometry(QtCore.QRect(140,100,51,21))
        self.open_time.setMinimum(1)
        self.open_time.setObjectName("open_time")

        self.open_password = QtGui.QLineEdit(WindowOpen)
        self.open_password.setGeometry(QtCore.QRect(120,60,190,21))
        self.open_password.setEchoMode(QtGui.QLineEdit.Password)
        self.open_password.setObjectName("open_password")

        self.open_path = QtGui.QLabel(WindowOpen)
        self.open_path.setGeometry(QtCore.QRect(120,20,190,21))
        self.open_path.setWordWrap(False)
        self.open_path.setObjectName("open_path")

        self.retranslateUi(WindowOpen)
        QtCore.QMetaObject.connectSlotsByName(WindowOpen)
        WindowOpen.setTabOrder(self.open_password,self.open_close)
        WindowOpen.setTabOrder(self.open_close,self.open_time)
        WindowOpen.setTabOrder(self.open_time,self.open_ok)
        WindowOpen.setTabOrder(self.open_ok,self.open_cancel)

    def retranslateUi(self, WindowOpen):
        WindowOpen.setWindowTitle(QtGui.QApplication.translate("WindowOpen", "Open an encrypted folder", None, QtGui.QApplication.UnicodeUTF8))
        self.open_ok.setText(QtGui.QApplication.translate("WindowOpen", "&OK", None, QtGui.QApplication.UnicodeUTF8))
        self.open_cancel.setText(QtGui.QApplication.translate("WindowOpen", "&Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1_2.setText(QtGui.QApplication.translate("WindowOpen", "Password:", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1_2_2.setText(QtGui.QApplication.translate("WindowOpen", "Path:", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel3.setText(QtGui.QApplication.translate("WindowOpen", "minutes of IDLE", None, QtGui.QApplication.UnicodeUTF8))
        self.open_close.setText(QtGui.QApplication.translate("WindowOpen", "Auto close after", None, QtGui.QApplication.UnicodeUTF8))

