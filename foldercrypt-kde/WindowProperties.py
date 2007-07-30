# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt3/WindowProperties.ui'
#
# Created: mar jui 31 00:16:35 2007
#      by: The PyQt User Interface Compiler (pyuic) 3.17
#
# WARNING! All changes made in this file will be lost!


from qt import *


class WindowProperties(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("WindowProperties")

        self.setSizeGripEnabled(1)


        self.textLabel1_2 = QLabel(self,"textLabel1_2")
        self.textLabel1_2.setGeometry(QRect(40,40,100,20))

        self.textLabel1 = QLabel(self,"textLabel1")
        self.textLabel1.setGeometry(QRect(40,10,100,20))

        self.textLabel1_3 = QLabel(self,"textLabel1_3")
        self.textLabel1_3.setGeometry(QRect(40,70,100,20))

        LayoutWidget = QWidget(self,"Layout1")
        LayoutWidget.setGeometry(QRect(20,130,320,33))
        Layout1 = QHBoxLayout(LayoutWidget,0,6,"Layout1")
        Horizontal_Spacing2 = QSpacerItem(20,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        Layout1.addItem(Horizontal_Spacing2)

        self.properties_ok = QPushButton(LayoutWidget,"properties_ok")
        self.properties_ok.setAutoDefault(1)
        self.properties_ok.setDefault(1)
        Layout1.addWidget(self.properties_ok)

        self.properties_cancel = QPushButton(LayoutWidget,"properties_cancel")
        self.properties_cancel.setAutoDefault(1)
        Layout1.addWidget(self.properties_cancel)

        self.textLabel1_4 = QLabel(self,"textLabel1_4")
        self.textLabel1_4.setGeometry(QRect(40,100,100,30))

        self.properties_old = QLineEdit(self,"properties_old")
        self.properties_old.setGeometry(QRect(150,40,171,21))
        self.properties_old.setEchoMode(QLineEdit.Password)

        self.properties_new = QLineEdit(self,"properties_new")
        self.properties_new.setGeometry(QRect(150,70,171,21))
        self.properties_new.setEchoMode(QLineEdit.Password)

        self.properties_confirm = QLineEdit(self,"properties_confirm")
        self.properties_confirm.setGeometry(QRect(150,100,171,21))
        self.properties_confirm.setEchoMode(QLineEdit.Password)

        self.properties_path = QLabel(self,"properties_path")
        self.properties_path.setGeometry(QRect(150,10,170,21))

        self.languageChange()

        self.resize(QSize(352,174).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.properties_ok,SIGNAL("clicked()"),self.accept)
        self.connect(self.properties_cancel,SIGNAL("clicked()"),self.reject)

        self.setTabOrder(self.properties_old,self.properties_new)
        self.setTabOrder(self.properties_new,self.properties_confirm)
        self.setTabOrder(self.properties_confirm,self.properties_ok)
        self.setTabOrder(self.properties_ok,self.properties_cancel)


    def languageChange(self):
        self.setCaption(self.__tr("Properties"))
        self.textLabel1_2.setText(self.__tr("Old password:"))
        self.textLabel1.setText(self.__tr("Path:"))
        self.textLabel1_3.setText(self.__tr("New password:"))
        self.properties_ok.setText(self.__tr("&OK"))
        self.properties_ok.setAccel(QKeySequence(QString.null))
        self.properties_cancel.setText(self.__tr("&Cancel"))
        self.properties_cancel.setAccel(QKeySequence(QString.null))
        self.textLabel1_4.setText(self.__tr("Confirmation:"))
        self.properties_path.setText(QString.null)


    def __tr(self,s,c = None):
        return qApp.translate("WindowProperties",s,c)
