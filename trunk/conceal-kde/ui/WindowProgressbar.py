# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'conceal-kde/qt3/WindowProgressbar.ui'
#
# Created: jeu aoû 16 13:03:28 2007
#      by: The PyQt User Interface Compiler (pyuic) 3.17
#
# WARNING! All changes made in this file will be lost!


from qt import *


class WindowProgressbar(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("WindowProgressbar")

        self.setModal(1)


        self.progressBar1 = QProgressBar(self,"progressBar1")
        self.progressBar1.setGeometry(QRect(0,0,280,23))
        self.progressBar1.setTotalSteps(0)
        self.progressBar1.setProgress(0)
        self.progressBar1.setPercentageVisible(0)

        self.languageChange()

        self.resize(QSize(279,21).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)


    def languageChange(self):
        self.setCaption(self.__tr("Processing..."))


    def __tr(self,s,c = None):
        return qApp.translate("WindowProgressbar",s,c)
