# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt3/WindowCrypt.ui'
#
# Created: mar jui 31 00:15:54 2007
#      by: The PyQt User Interface Compiler (pyuic) 3.17
#
# WARNING! All changes made in this file will be lost!


from qt import *


class WindowCrypt(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("WindowCrypt")



        self.textLabel1_2 = QLabel(self,"textLabel1_2")
        self.textLabel1_2.setGeometry(QRect(10,50,91,21))

        self.textLabel1_2_2 = QLabel(self,"textLabel1_2_2")
        self.textLabel1_2_2.setGeometry(QRect(10,80,91,21))

        self.textLabel1 = QLabel(self,"textLabel1")
        self.textLabel1.setGeometry(QRect(10,20,91,21))

        LayoutWidget = QWidget(self,"Layout1")
        LayoutWidget.setGeometry(QRect(0,120,300,33))
        Layout1 = QHBoxLayout(LayoutWidget,0,6,"Layout1")
        Horizontal_Spacing2 = QSpacerItem(20,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        Layout1.addItem(Horizontal_Spacing2)

        self.crypt_ok = QPushButton(LayoutWidget,"crypt_ok")
        self.crypt_ok.setAutoDefault(1)
        self.crypt_ok.setDefault(1)
        Layout1.addWidget(self.crypt_ok)

        self.crypt_cancel = QPushButton(LayoutWidget,"crypt_cancel")
        self.crypt_cancel.setAutoDefault(1)
        Layout1.addWidget(self.crypt_cancel)

        self.crypt_confirmation = QLineEdit(self,"crypt_confirmation")
        self.crypt_confirmation.setGeometry(QRect(110,80,190,21))
        self.crypt_confirmation.setEchoMode(QLineEdit.Password)

        self.crypt_file = QPushButton(self,"crypt_file")
        self.crypt_file.setGeometry(QRect(230,20,70,21))

        self.crypt_password = QLineEdit(self,"crypt_password")
        self.crypt_password.setGeometry(QRect(110,50,190,21))
        self.crypt_password.setEchoMode(QLineEdit.Password)

        self.crypt_path = QLineEdit(self,"crypt_path")
        self.crypt_path.setGeometry(QRect(110,20,120,21))
        self.crypt_path.setEchoMode(QLineEdit.Normal)

        self.languageChange()

        self.resize(QSize(315,173).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.setTabOrder(self.crypt_path,self.crypt_file)
        self.setTabOrder(self.crypt_file,self.crypt_password)
        self.setTabOrder(self.crypt_password,self.crypt_confirmation)
        self.setTabOrder(self.crypt_confirmation,self.crypt_ok)
        self.setTabOrder(self.crypt_ok,self.crypt_cancel)


    def languageChange(self):
        self.setCaption(self.__tr("Encrypt"))
        self.textLabel1_2.setText(self.__tr("Password:"))
        self.textLabel1_2_2.setText(self.__tr("Confirmation:"))
        self.textLabel1.setText(self.__tr("Path:"))
        self.crypt_ok.setText(self.__tr("&OK"))
        self.crypt_ok.setAccel(QKeySequence(QString.null))
        self.crypt_cancel.setText(self.__tr("&Cancel"))
        self.crypt_cancel.setAccel(QKeySequence(QString.null))
        self.crypt_file.setText(self.__tr("Choose..."))


    def __tr(self,s,c = None):
        return qApp.translate("WindowCrypt",s,c)
