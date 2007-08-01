# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt3/WindowOpen.ui'
#
# Created: mar jui 31 00:17:03 2007
#      by: The PyQt User Interface Compiler (pyuic) 3.17
#
# WARNING! All changes made in this file will be lost!


from qt import *


class WindowOpen(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("WindowOpen")

        self.setSizeGripEnabled(1)


        LayoutWidget = QWidget(self,"Layout1")
        LayoutWidget.setGeometry(QRect(10,130,300,33))
        Layout1 = QHBoxLayout(LayoutWidget,0,6,"Layout1")
        Horizontal_Spacing2 = QSpacerItem(20,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        Layout1.addItem(Horizontal_Spacing2)

        self.open_ok = QPushButton(LayoutWidget,"open_ok")
        self.open_ok.setAutoDefault(1)
        self.open_ok.setDefault(1)
        Layout1.addWidget(self.open_ok)

        self.open_cancel = QPushButton(LayoutWidget,"open_cancel")
        self.open_cancel.setAutoDefault(1)
        Layout1.addWidget(self.open_cancel)

        self.textLabel1_2 = QLabel(self,"textLabel1_2")
        self.textLabel1_2.setGeometry(QRect(10,60,91,21))

        self.textLabel1_2_2 = QLabel(self,"textLabel1_2_2")
        self.textLabel1_2_2.setGeometry(QRect(10,20,91,21))

        self.textLabel3 = QLabel(self,"textLabel3")
        self.textLabel3.setGeometry(QRect(200,100,110,21))

        self.open_close = QCheckBox(self,"open_close")
        self.open_close.setGeometry(QRect(10,100,130,21))

        self.open_time = QSpinBox(self,"open_time")
        self.open_time.setEnabled(0)
        self.open_time.setGeometry(QRect(140,100,51,21))
        self.open_time.setMinValue(1)

        self.open_password = QLineEdit(self,"open_password")
        self.open_password.setGeometry(QRect(120,60,190,21))
        self.open_password.setEchoMode(QLineEdit.Password)

        self.open_path = QLabel(self,"open_path")
        self.open_path.setGeometry(QRect(120,20,190,21))

        self.languageChange()

        self.resize(QSize(324,188).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.setTabOrder(self.open_password,self.open_close)
        self.setTabOrder(self.open_close,self.open_time)
        self.setTabOrder(self.open_time,self.open_ok)
        self.setTabOrder(self.open_ok,self.open_cancel)


    def languageChange(self):
        self.setCaption(self.__tr("Open an encrypted folder"))
        self.open_ok.setText(self.__tr("&OK"))
        self.open_ok.setAccel(QKeySequence(QString.null))
        self.open_cancel.setText(self.__tr("&Cancel"))
        self.open_cancel.setAccel(QKeySequence(QString.null))
        self.textLabel1_2.setText(self.__tr("Password:"))
        self.textLabel1_2_2.setText(self.__tr("Path:"))
        self.textLabel3.setText(self.__tr("minutes of IDLE"))
        self.open_close.setText(self.__tr("Auto close after"))
        self.open_path.setText(QString.null)


    def __tr(self,s,c = None):
        return qApp.translate("WindowOpen",s,c)
