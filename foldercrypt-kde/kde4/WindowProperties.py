# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt4/WindowProperties.ui'
#
# Created: Mon Jul 30 20:30:28 2007
#      by: PyQt4 UI code generator 4.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_WindowProperties(object):
    def setupUi(self, WindowProperties):
        WindowProperties.setObjectName("WindowProperties")
        WindowProperties.resize(QtCore.QSize(QtCore.QRect(0,0,352,174).size()).expandedTo(WindowProperties.minimumSizeHint()))
        WindowProperties.setSizeGripEnabled(True)

        self.textLabel1_2 = QtGui.QLabel(WindowProperties)
        self.textLabel1_2.setGeometry(QtCore.QRect(40,40,100,20))
        self.textLabel1_2.setWordWrap(False)
        self.textLabel1_2.setObjectName("textLabel1_2")

        self.textLabel1 = QtGui.QLabel(WindowProperties)
        self.textLabel1.setGeometry(QtCore.QRect(40,10,100,20))
        self.textLabel1.setWordWrap(False)
        self.textLabel1.setObjectName("textLabel1")

        self.textLabel1_3 = QtGui.QLabel(WindowProperties)
        self.textLabel1_3.setGeometry(QtCore.QRect(40,70,100,20))
        self.textLabel1_3.setWordWrap(False)
        self.textLabel1_3.setObjectName("textLabel1_3")

        self.Layout1 = QtGui.QWidget(WindowProperties)
        self.Layout1.setGeometry(QtCore.QRect(20,130,320,33))
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

        self.properties_ok = QtGui.QPushButton(self.Layout1)
        self.properties_ok.setAutoDefault(True)
        self.properties_ok.setDefault(True)
        self.properties_ok.setObjectName("properties_ok")
        self.hboxlayout.addWidget(self.properties_ok)

        self.properties_cancel = QtGui.QPushButton(self.Layout1)
        self.properties_cancel.setAutoDefault(True)
        self.properties_cancel.setObjectName("properties_cancel")
        self.hboxlayout.addWidget(self.properties_cancel)

        self.textLabel1_4 = QtGui.QLabel(WindowProperties)
        self.textLabel1_4.setGeometry(QtCore.QRect(40,100,100,30))
        self.textLabel1_4.setWordWrap(False)
        self.textLabel1_4.setObjectName("textLabel1_4")

        self.properties_old = QtGui.QLineEdit(WindowProperties)
        self.properties_old.setGeometry(QtCore.QRect(150,40,171,21))
        self.properties_old.setEchoMode(QtGui.QLineEdit.Password)
        self.properties_old.setObjectName("properties_old")

        self.properties_new = QtGui.QLineEdit(WindowProperties)
        self.properties_new.setGeometry(QtCore.QRect(150,70,171,21))
        self.properties_new.setEchoMode(QtGui.QLineEdit.Password)
        self.properties_new.setObjectName("properties_new")

        self.properties_confirm = QtGui.QLineEdit(WindowProperties)
        self.properties_confirm.setGeometry(QtCore.QRect(150,100,171,21))
        self.properties_confirm.setEchoMode(QtGui.QLineEdit.Password)
        self.properties_confirm.setObjectName("properties_confirm")

        self.properties_path = QtGui.QLabel(WindowProperties)
        self.properties_path.setGeometry(QtCore.QRect(150,10,170,21))
        self.properties_path.setWordWrap(False)
        self.properties_path.setObjectName("properties_path")

        self.retranslateUi(WindowProperties)
        QtCore.QObject.connect(self.properties_ok,QtCore.SIGNAL("clicked()"),WindowProperties.accept)
        QtCore.QObject.connect(self.properties_cancel,QtCore.SIGNAL("clicked()"),WindowProperties.reject)
        QtCore.QMetaObject.connectSlotsByName(WindowProperties)
        WindowProperties.setTabOrder(self.properties_old,self.properties_new)
        WindowProperties.setTabOrder(self.properties_new,self.properties_confirm)
        WindowProperties.setTabOrder(self.properties_confirm,self.properties_ok)
        WindowProperties.setTabOrder(self.properties_ok,self.properties_cancel)

    def retranslateUi(self, WindowProperties):
        WindowProperties.setWindowTitle(QtGui.QApplication.translate("WindowProperties", "Properties", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1_2.setText(QtGui.QApplication.translate("WindowProperties", "Old password:", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1.setText(QtGui.QApplication.translate("WindowProperties", "Path:", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1_3.setText(QtGui.QApplication.translate("WindowProperties", "New password:", None, QtGui.QApplication.UnicodeUTF8))
        self.properties_ok.setText(QtGui.QApplication.translate("WindowProperties", "&OK", None, QtGui.QApplication.UnicodeUTF8))
        self.properties_cancel.setText(QtGui.QApplication.translate("WindowProperties", "&Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1_4.setText(QtGui.QApplication.translate("WindowProperties", "Confirmation:", None, QtGui.QApplication.UnicodeUTF8))

