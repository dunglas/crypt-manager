# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WindowDecrypt.ui'
#
# Created: ven jui 27 19:14:02 2007
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


        self.decrypt_path = QLabel(self,"decrypt_path")
        self.decrypt_path.setGeometry(QRect(30,30,60,20))

        self.decrypt_password2 = QLabel(self,"decrypt_password2")
        self.decrypt_password2.setGeometry(QRect(30,60,70,20))

        self.decrypt_password = QLineEdit(self,"decrypt_password")
        self.decrypt_password.setGeometry(QRect(110,60,250,22))

        self.textLabel2 = QLabel(self,"textLabel2")
        self.textLabel2.setGeometry(QRect(110,30,251,21))

        LayoutWidget = QWidget(self,"Layout1")
        LayoutWidget.setGeometry(QRect(20,90,360,33))
        Layout1 = QHBoxLayout(LayoutWidget,0,6,"Layout1")
        Horizontal_Spacing2 = QSpacerItem(20,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        Layout1.addItem(Horizontal_Spacing2)

        self.buttonOk = QPushButton(LayoutWidget,"buttonOk")
        self.buttonOk.setAutoDefault(1)
        self.buttonOk.setDefault(1)
        Layout1.addWidget(self.buttonOk)

        self.buttonCancel = QPushButton(LayoutWidget,"buttonCancel")
        self.buttonCancel.setAutoDefault(1)
        Layout1.addWidget(self.buttonCancel)

        self.languageChange()

        self.resize(QSize(391,139).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.buttonOk,SIGNAL("clicked()"),self.accept)
        self.connect(self.buttonCancel,SIGNAL("clicked()"),self.reject)


    def languageChange(self):
        self.setCaption(self.__tr("Decrypt"))
        self.decrypt_path.setText(self.__tr("Path:"))
        self.decrypt_password2.setText(self.__tr("Password:"))
        self.textLabel2.setText(QString.null)
        self.buttonOk.setText(self.__tr("&OK"))
        self.buttonOk.setAccel(QKeySequence(QString.null))
        self.buttonCancel.setText(self.__tr("&Cancel"))
        self.buttonCancel.setAccel(QKeySequence(QString.null))


    def __tr(self,s,c = None):
        return qApp.translate("WindowDecrypt",s,c)
