# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'arayuz_bim.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1028, 814)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.building = QtWidgets.QComboBox(self.centralwidget)
        self.building.setGeometry(QtCore.QRect(820, 70, 181, 51))
        self.building.setMinimumSize(QtCore.QSize(181, 0))
        self.building.setEditable(False)
        self.building.setObjectName("building")
        self.building.addItem("")
        self.building.addItem("")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(790, 0, 16, 781))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.building_2 = QtWidgets.QComboBox(self.centralwidget)
        self.building_2.setGeometry(QtCore.QRect(820, 160, 181, 51))
        self.building_2.setMinimumSize(QtCore.QSize(181, 0))
        self.building_2.setEditable(False)
        self.building_2.setObjectName("building_2")
        self.building_2.addItem("")
        self.building_2.addItem("")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(820, 20, 121, 41))
        self.textEdit.setObjectName("textEdit")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(820, 130, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1028, 26))
        self.menubar.setObjectName("menubar")
        self.menuBIM = QtWidgets.QMenu(self.menubar)
        self.menuBIM.setObjectName("menuBIM")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuBIM.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.building.setCurrentText(_translate("MainWindow", "GSU"))
        self.building.setItemText(0, _translate("MainWindow", "GSU"))
        self.building.setItemText(1, _translate("MainWindow", "INSA"))
        self.building_2.setCurrentText(_translate("MainWindow", "Mr. Pinarer"))
        self.building_2.setItemText(0, _translate("MainWindow", "Mr. Pinarer"))
        self.building_2.setItemText(1, _translate("MainWindow", "A324"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">BUILDING</span></p></body></html>"))
        self.lineEdit.setText(_translate("MainWindow", "ROOM"))
        self.menuBIM.setTitle(_translate("MainWindow", "BIM"))
