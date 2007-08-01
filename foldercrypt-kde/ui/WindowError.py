# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt3/WindowError.ui'
#
# Created: mar jui 31 00:16:04 2007
#      by: The PyQt User Interface Compiler (pyuic) 3.17
#
# WARNING! All changes made in this file will be lost!


from qt import *


class WindowError(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("WindowError")

        self.setSizeGripEnabled(1)


        LayoutWidget = QWidget(self,"Layout1")
        LayoutWidget.setGeometry(QRect(20,100,240,26))
        Layout1 = QHBoxLayout(LayoutWidget,0,6,"Layout1")
        Horizontal_Spacing2 = QSpacerItem(20,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        Layout1.addItem(Horizontal_Spacing2)

        self.error_ok = QPushButton(LayoutWidget,"error_ok")
        self.error_ok.setAutoDefault(1)
        self.error_ok.setDefault(1)
        Layout1.addWidget(self.error_ok)

        self.error_msg = QLabel(self,"error_msg")
        self.error_msg.setGeometry(QRect(30,30,220,50))

        self.languageChange()

        self.resize(QSize(273,136).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.error_ok,SIGNAL("clicked()"),self.accept)


    def languageChange(self):
        self.setCaption(self.__tr("Error"))
        self.error_ok.setText(self.__tr("&OK"))
        self.error_ok.setAccel(QKeySequence(QString.null))
        self.error_msg.setText(QString.null)


    def __tr(self,s,c = None):
        return qApp.translate("WindowError",s,c)
