# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_v2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.building = QtWidgets.QComboBox(self.centralwidget)
        self.building.setGeometry(QtCore.QRect(490, 60, 191, 40))
        self.building.setMinimumSize(QtCore.QSize(181, 0))
        self.building.setEditable(False)
        self.building.setObjectName("building")
        self.building.addItem("")
        self.building.addItem("")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(470, 0, 16, 530))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.floor = QtWidgets.QComboBox(self.centralwidget)
        self.floor.setGeometry(QtCore.QRect(490, 170, 191, 40))
        self.floor.setMinimumSize(QtCore.QSize(181, 0))
        self.floor.setEditable(False)
        self.floor.setObjectName("floor")
        self.floor.addItem("")
        self.floor.addItem("")
        self.buildingText = QtWidgets.QTextEdit(self.centralwidget)
        self.buildingText.setGeometry(QtCore.QRect(490, 10, 91, 41))
        self.buildingText.setObjectName("buildingText")
        self.tempLog = QtWidgets.QTextBrowser(self.centralwidget)
        self.tempLog.setGeometry(QtCore.QRect(10, 400, 91, 121))
        self.tempLog.setObjectName("tempLog")
        self.myWindow = QtWidgets.QLabel(self.centralwidget)
        self.myWindow.setGeometry(QtCore.QRect(10, 0, 461, 351))
        self.myWindow.setText("")
        self.myWindow.setPixmap(QtGui.QPixmap("bim_sized.jpg"))
        self.myWindow.setObjectName("myWindow")
        self.floorText = QtWidgets.QTextEdit(self.centralwidget)
        self.floorText.setGeometry(QtCore.QRect(490, 120, 61, 41))
        self.floorText.setObjectName("floorText")
        self.sensorText = QtWidgets.QTextEdit(self.centralwidget)
        self.sensorText.setGeometry(QtCore.QRect(490, 340, 191, 41))
        self.sensorText.setObjectName("sensorText")
        self.streamButton = QtWidgets.QPushButton(self.centralwidget)
        self.streamButton.setGeometry(QtCore.QRect(490, 460, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.streamButton.setFont(font)
        self.streamButton.setObjectName("streamButton")
        self.room = QtWidgets.QComboBox(self.centralwidget)
        self.room.setGeometry(QtCore.QRect(490, 280, 191, 40))
        self.room.setMinimumSize(QtCore.QSize(181, 0))
        self.room.setEditable(False)
        self.room.setObjectName("room")
        self.room.addItem("")
        self.room.addItem("")
        self.roomText = QtWidgets.QTextEdit(self.centralwidget)
        self.roomText.setGeometry(QtCore.QRect(490, 230, 71, 41))
        self.roomText.setObjectName("roomText")
        self.humidityLog = QtWidgets.QTextBrowser(self.centralwidget)
        self.humidityLog.setGeometry(QtCore.QRect(110, 400, 81, 121))
        self.humidityLog.setObjectName("humidityLog")
        self.co2Log = QtWidgets.QTextBrowser(self.centralwidget)
        self.co2Log.setGeometry(QtCore.QRect(200, 400, 81, 121))
        self.co2Log.setObjectName("co2Log")
        self.lightLog = QtWidgets.QTextBrowser(self.centralwidget)
        self.lightLog.setGeometry(QtCore.QRect(290, 400, 81, 121))
        self.lightLog.setObjectName("lightLog")
        self.presenceLog = QtWidgets.QTextBrowser(self.centralwidget)
        self.presenceLog.setGeometry(QtCore.QRect(380, 400, 81, 121))
        self.presenceLog.setObjectName("presenceLog")
        self.tempText = QtWidgets.QTextEdit(self.centralwidget)
        self.tempText.setGeometry(QtCore.QRect(10, 360, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.tempText.setFont(font)
        self.tempText.setObjectName("tempText")
        self.humidityText = QtWidgets.QTextEdit(self.centralwidget)
        self.humidityText.setGeometry(QtCore.QRect(110, 360, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.humidityText.setFont(font)
        self.humidityText.setObjectName("humidityText")
        self.co2Text = QtWidgets.QTextEdit(self.centralwidget)
        self.co2Text.setGeometry(QtCore.QRect(200, 360, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.co2Text.setFont(font)
        self.co2Text.setObjectName("co2Text")
        self.LightText = QtWidgets.QTextEdit(self.centralwidget)
        self.LightText.setGeometry(QtCore.QRect(290, 360, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.LightText.setFont(font)
        self.LightText.setObjectName("LightText")
        self.presenceText = QtWidgets.QTextEdit(self.centralwidget)
        self.presenceText.setGeometry(QtCore.QRect(380, 360, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.presenceText.setFont(font)
        self.presenceText.setObjectName("presenceText")
        self.temperature = QtWidgets.QCheckBox(self.centralwidget)
        self.temperature.setGeometry(QtCore.QRect(490, 390, 111, 20))
        self.temperature.setObjectName("temperature")
        self.humidity = QtWidgets.QCheckBox(self.centralwidget)
        self.humidity.setGeometry(QtCore.QRect(600, 390, 81, 20))
        self.humidity.setObjectName("humidity")
        self.co2 = QtWidgets.QCheckBox(self.centralwidget)
        self.co2.setGeometry(QtCore.QRect(490, 410, 81, 20))
        self.co2.setObjectName("co2")
        self.light = QtWidgets.QCheckBox(self.centralwidget)
        self.light.setGeometry(QtCore.QRect(600, 410, 81, 20))
        self.light.setObjectName("light")
        self.presence = QtWidgets.QCheckBox(self.centralwidget)
        self.presence.setGeometry(QtCore.QRect(490, 430, 81, 20))
        self.presence.setObjectName("presence")
        self.myLog = QtWidgets.QTextEdit(self.centralwidget)
        self.myLog.setGeometry(QtCore.QRect(10, 530, 671, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.myLog.setFont(font)
        self.myLog.setObjectName("myLog")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 26))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Building Information Modeling"))
        self.building.setCurrentText(_translate("MainWindow", "deneme1"))
        self.building.setItemText(0, _translate("MainWindow", "deneme1"))
        self.building.setItemText(1, _translate("MainWindow", "deneme2"))
        self.floor.setCurrentText(_translate("MainWindow", "First Floor"))
        self.floor.setItemText(0, _translate("MainWindow", "First Floor"))
        self.floor.setItemText(1, _translate("MainWindow", "Second Floor"))
        self.buildingText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Building</span></p></body></html>"))
        self.floorText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Floor</span></p></body></html>"))
        self.sensorText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Available Services</span></p></body></html>"))
        self.streamButton.setText(_translate("MainWindow", "START STREAMING"))
        self.room.setCurrentText(_translate("MainWindow", "room1"))
        self.room.setItemText(0, _translate("MainWindow", "room1"))
        self.room.setItemText(1, _translate("MainWindow", "room2"))
        self.roomText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Room</span></p></body></html>"))
        self.tempText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Temperature</p></body></html>"))
        self.humidityText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Humidity</p></body></html>"))
        self.co2Text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Co2</p></body></html>"))
        self.LightText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Light</p></body></html>"))
        self.presenceText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Presence</p></body></html>"))
        self.temperature.setText(_translate("MainWindow", "Temperature"))
        self.humidity.setText(_translate("MainWindow", "Humidity"))
        self.co2.setText(_translate("MainWindow", "Co2"))
        self.light.setText(_translate("MainWindow", "Light"))
        self.presence.setText(_translate("MainWindow", "Presence"))
        self.myLog.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">myLog</span></p></body></html>"))
        self.menuBIM.setTitle(_translate("MainWindow", "BIM"))

