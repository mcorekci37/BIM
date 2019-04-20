# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'arayuz_bim.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        # MainWindow.resize(1029, 814)
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.building = QtWidgets.QComboBox(self.centralwidget)
        # self.building.setGeometry(QtCore.QRect(820, 70, 181, 51))
        self.building.setGeometry(QtCore.QRect(600, 70, 181, 51))
        self.building.setMinimumSize(QtCore.QSize(181, 0))
        self.building.setEditable(False)
        self.building.setObjectName("building")
        self.building.addItem("")
        self.building.addItem("")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(580, 0, 16, 781))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.room = QtWidgets.QComboBox(self.centralwidget)
        self.room.setGeometry(QtCore.QRect(600, 200, 181, 51))
        self.room.setMinimumSize(QtCore.QSize(181, 0))
        self.room.setEditable(False)
        self.room.setObjectName("room")
        self.room.addItem("")
        self.room.addItem("")
        self.buildingText = QtWidgets.QTextEdit(self.centralwidget)
        self.buildingText.setGeometry(QtCore.QRect(600, 20, 121, 41))
        self.buildingText.setObjectName("buildingText")
        self.myLog = QtWidgets.QTextBrowser(self.centralwidget)
        self.myLog.setGeometry(QtCore.QRect(10, 420, 560, 150))
        self.myLog.setObjectName("myLog")
        self.myWindow = QtWidgets.QLabel(self.centralwidget)
        self.myWindow.setGeometry(QtCore.QRect(10, 10, 560, 400))
        self.myWindow.setText("")
        self.myWindow.setObjectName("myWindow")
        self.roomText = QtWidgets.QTextEdit(self.centralwidget)
        self.roomText.setGeometry(QtCore.QRect(600, 150, 121, 41))
        self.roomText.setObjectName("roomText")
        self.sensor = QtWidgets.QComboBox(self.centralwidget)
        self.sensor.setGeometry(QtCore.QRect(600, 330, 181, 51))
        self.sensor.setMinimumSize(QtCore.QSize(181, 0))
        self.sensor.setEditable(False)
        self.sensor.setObjectName("sensor")
        self.sensor.addItem("")
        self.sensor.addItem("")
        self.sensorText = QtWidgets.QTextEdit(self.centralwidget)
        self.sensorText.setGeometry(QtCore.QRect(600, 280, 121, 41))
        self.sensorText.setObjectName("sensorText")
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(600, 420, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.clearButton.setFont(font)
        self.clearButton.setObjectName("clearButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1029, 26))
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
        self.building.setCurrentText(_translate("MainWindow", "deneme1"))
        self.building.setItemText(0, _translate("MainWindow", "deneme1"))
        self.building.setItemText(1, _translate("MainWindow", "deneme2"))
        self.room.setCurrentText(_translate("MainWindow", "room1"))
        self.room.setItemText(0, _translate("MainWindow", "room1"))
        self.room.setItemText(1, _translate("MainWindow", "room2"))
        self.buildingText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">BUILDING</span></p></body></html>"))
        self.roomText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">ROOM</span></p></body></html>"))
        self.sensor.setCurrentText(_translate("MainWindow", "sensor1"))
        self.sensor.setItemText(0, _translate("MainWindow", "sensor1"))
        self.sensor.setItemText(1, _translate("MainWindow", "sensor2"))
        self.sensorText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">AVAILABLE SERVICES</span></p></body></html>"))
        self.clearButton.setText(_translate("MainWindow", "START STREAMING"))
        self.menuBIM.setTitle(_translate("MainWindow", "BIM"))


