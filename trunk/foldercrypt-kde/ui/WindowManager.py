# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt3/WindowManager.ui'
#
# Created: mar jui 31 00:16:54 2007
#      by: The PyQt User Interface Compiler (pyuic) 3.17
#
# WARNING! All changes made in this file will be lost!


from qt import *


class WindowManager(QMainWindow):
    def __init__(self,parent = None,name = None,fl = 0):
        QMainWindow.__init__(self,parent,name,fl)
        self.statusBar()

        if not name:
            self.setName("WindowManager")


        self.setCentralWidget(QWidget(self,"qt_central_widget"))

        self.manager_reset = QPushButton(self.centralWidget(),"manager_reset")
        self.manager_reset.setGeometry(QRect(390,400,90,30))

        self.manager_apply = QPushButton(self.centralWidget(),"manager_apply")
        self.manager_apply.setGeometry(QRect(490,400,90,30))

        self.manager_crypt = QPushButton(self.centralWidget(),"manager_crypt")
        self.manager_crypt.setGeometry(QRect(490,30,90,30))

        self.manager_properties = QPushButton(self.centralWidget(),"manager_properties")
        self.manager_properties.setEnabled(0)
        self.manager_properties.setGeometry(QRect(490,110,90,30))

        self.manager_decrypt = QPushButton(self.centralWidget(),"manager_decrypt")
        self.manager_decrypt.setEnabled(0)
        self.manager_decrypt.setGeometry(QRect(490,150,90,30))

        self.manager_list = QListView(self.centralWidget(),"manager_list")
        self.manager_list.addColumn(QString.null)
        self.manager_list.addColumn(self.__tr("Path"))
        self.manager_list.addColumn(self.__tr("Open"))
        self.manager_list.setGeometry(QRect(30,30,450,360))
        self.manager_list.setAllColumnsShowFocus(0)

        self.manager_open_close = QPushButton(self.centralWidget(),"manager_open_close")
        self.manager_open_close.setEnabled(0)
        self.manager_open_close.setGeometry(QRect(490,70,90,30))



        self.languageChange()

        self.resize(QSize(621,480).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.setTabOrder(self.manager_list,self.manager_crypt)
        self.setTabOrder(self.manager_crypt,self.manager_open_close)
        self.setTabOrder(self.manager_open_close,self.manager_properties)
        self.setTabOrder(self.manager_properties,self.manager_decrypt)
        self.setTabOrder(self.manager_decrypt,self.manager_reset)
        self.setTabOrder(self.manager_reset,self.manager_apply)


    def languageChange(self):
        self.setCaption(self.__tr("Manager"))
        self.manager_reset.setText(self.__tr("Reset"))
        self.manager_apply.setText(self.__tr("Apply"))
        self.manager_crypt.setText(self.__tr("Encrypt"))
        self.manager_properties.setText(self.__tr("Properties"))
        self.manager_decrypt.setText(self.__tr("Decrypt"))
        self.manager_list.header().setLabel(0,QString.null)
        self.manager_list.header().setLabel(1,self.__tr("Path"))
        self.manager_list.header().setLabel(2,self.__tr("Open"))
        self.manager_open_close.setText(self.__tr("Open"))


    def __tr(self,s,c = None):
        return qApp.translate("WindowManager",s,c)
