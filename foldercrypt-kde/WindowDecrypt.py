# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt3/WindowDecrypt.ui'
#
# Created: lun jui 30 15:41:30 2007
#      by: The PyQt User Interface Compiler (pyuic) 3.17
#
# WARNING! All changes made in this file will be lost!


from qt import *


class WindowDecrypt(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("WindowDecrypt")

        self.setSizeGripEnabled(1)


        self.decrypt_password2 = QLabel(self,"decrypt_password2")
        self.decrypt_password2.setGeometry(QRect(30,60,70,20))

        LayoutWidget = QWidget(self,"Layout1")
        LayoutWidget.setGeometry(QRect(20,90,250,33))
        Layout1 = QHBoxLayout(LayoutWidget,0,6,"Layout1")
        Horizontal_Spacing2 = QSpacerItem(20,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        Layout1.addItem(Horizontal_Spacing2)

        self.decrypt_ok = QPushButton(LayoutWidget,"decrypt_ok")
        self.decrypt_ok.setAutoDefault(1)
        self.decrypt_ok.setDefault(1)
        Layout1.addWidget(self.decrypt_ok)

        self.decrypt_cancel = QPushButton(LayoutWidget,"decrypt_cancel")
        self.decrypt_cancel.setAutoDefault(1)
        Layout1.addWidget(self.decrypt_cancel)

        self.decrypt_path = QLabel(self,"decrypt_path")
        self.decrypt_path.setGeometry(QRect(30,30,60,20))

        self.decrypt_password = QLineEdit(self,"decrypt_password")
        self.decrypt_password.setGeometry(QRect(110,60,150,22))
        self.decrypt_password.setEchoMode(QLineEdit.Password)

        self.textLabel2 = QLabel(self,"textLabel2")
        self.textLabel2.setGeometry(QRect(110,30,250,21))

        self.languageChange()

        self.resize(QSize(283,139).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.decrypt_ok,SIGNAL("clicked()"),self.accept)
        self.connect(self.decrypt_cancel,SIGNAL("clicked()"),self.reject)


    def languageChange(self):
        self.setCaption(self.__tr("Decrypt"))
        self.decrypt_password2.setText(self.__tr("Password:"))
        self.decrypt_ok.setText(self.__tr("&OK"))
        self.decrypt_ok.setAccel(QKeySequence(QString.null))
        self.decrypt_cancel.setText(self.__tr("&Cancel"))
        self.decrypt_cancel.setAccel(QKeySequence(QString.null))
        self.decrypt_path.setText(self.__tr("Path:"))
        self.textLabel2.setText(QString.null)


    def __tr(self,s,c = None):
        return qApp.translate("WindowDecrypt",s,c)
