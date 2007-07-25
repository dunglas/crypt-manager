# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crypt.ui'
#
# Created: mer jui 25 11:12:01 2007
#      by: The PyQt User Interface Compiler (pyuic) 3.17
#
# WARNING! All changes made in this file will be lost!


from qt import *


class crypt(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("crypt")



        self.textLabel1_2 = QLabel(self,"textLabel1_2")
        self.textLabel1_2.setGeometry(QRect(10,50,91,21))

        self.textLabel1_2_2 = QLabel(self,"textLabel1_2_2")
        self.textLabel1_2_2.setGeometry(QRect(10,80,91,21))

        self.crypt_confirmation = QLineEdit(self,"crypt_confirmation")
        self.crypt_confirmation.setGeometry(QRect(110,80,190,21))

        self.textLabel1 = QLabel(self,"textLabel1")
        self.textLabel1.setGeometry(QRect(10,20,91,21))

        self.crypt_path = QLineEdit(self,"crypt_path")
        self.crypt_path.setGeometry(QRect(111,20,190,21))

        self.crypt_password = QLineEdit(self,"crypt_password")
        self.crypt_password.setGeometry(QRect(110,50,190,21))

        LayoutWidget = QWidget(self,"Layout1")
        LayoutWidget.setGeometry(QRect(0,120,300,33))
        Layout1 = QHBoxLayout(LayoutWidget,0,6,"Layout1")

        self.crypt_help = QPushButton(LayoutWidget,"crypt_help")
        self.crypt_help.setAutoDefault(1)
        Layout1.addWidget(self.crypt_help)
        Horizontal_Spacing2 = QSpacerItem(20,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        Layout1.addItem(Horizontal_Spacing2)

        self.crypt_ok = QPushButton(LayoutWidget,"crypt_ok")
        self.crypt_ok.setAutoDefault(1)
        self.crypt_ok.setDefault(1)
        Layout1.addWidget(self.crypt_ok)

        self.crypt_cancel = QPushButton(LayoutWidget,"crypt_cancel")
        self.crypt_cancel.setAutoDefault(1)
        Layout1.addWidget(self.crypt_cancel)

        self.languageChange()

        self.resize(QSize(610,610).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)


    def languageChange(self):
        self.setCaption(self.__tr("Encrypt"))
        self.textLabel1_2.setText(self.__tr("Password:"))
        self.textLabel1_2_2.setText(self.__tr("Confirmation:"))
        self.textLabel1.setText(self.__tr("Path:"))
        self.crypt_help.setText(self.__tr("&Help"))
        self.crypt_help.setAccel(QKeySequence(self.__tr("F1")))
        self.crypt_ok.setText(self.__tr("&OK"))
        self.crypt_ok.setAccel(QKeySequence(QString.null))
        self.crypt_cancel.setText(self.__tr("&Cancel"))
        self.crypt_cancel.setAccel(QKeySequence(QString.null))


    def __tr(self,s,c = None):
        return qApp.translate("crypt",s,c)
