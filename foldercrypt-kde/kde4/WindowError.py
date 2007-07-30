# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt4/WindowError.ui'
#
# Created: Mon Jul 30 20:29:32 2007
#      by: PyQt4 UI code generator 4.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_WindowError(object):
    def setupUi(self, WindowError):
        WindowError.setObjectName("WindowError")
        WindowError.resize(QtCore.QSize(QtCore.QRect(0,0,273,136).size()).expandedTo(WindowError.minimumSizeHint()))
        WindowError.setSizeGripEnabled(True)

        self.Layout1 = QtGui.QWidget(WindowError)
        self.Layout1.setGeometry(QtCore.QRect(20,100,240,26))
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

        self.error_ok = QtGui.QPushButton(self.Layout1)
        self.error_ok.setAutoDefault(True)
        self.error_ok.setDefault(True)
        self.error_ok.setObjectName("error_ok")
        self.hboxlayout.addWidget(self.error_ok)

        self.error_msg = QtGui.QLabel(WindowError)
        self.error_msg.setGeometry(QtCore.QRect(30,30,220,50))
        self.error_msg.setWordWrap(False)
        self.error_msg.setObjectName("error_msg")

        self.retranslateUi(WindowError)
        QtCore.QObject.connect(self.error_ok,QtCore.SIGNAL("clicked()"),WindowError.accept)
        QtCore.QMetaObject.connectSlotsByName(WindowError)

    def retranslateUi(self, WindowError):
        WindowError.setWindowTitle(QtGui.QApplication.translate("WindowError", "Error", None, QtGui.QApplication.UnicodeUTF8))
        self.error_ok.setText(QtGui.QApplication.translate("WindowError", "&OK", None, QtGui.QApplication.UnicodeUTF8))

