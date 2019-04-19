from arayuz_bim import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui, QtCore
import sys
import Building
import Room
import Sensor

from Main import Service as service



class ProjectUi(QtWidgets.QMainWindow):
    def __init__(self,buildings):
        self.buildings = buildings
        self.currentBuilding=None
        self.currentRoom=None
        self.currentSensor=None

        self.qt_app = QtWidgets.QApplication(sys.argv)
        QtWidgets.QWidget.__init__(self, None)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # self.ui.textEdit
        # self.ui.lineEdit
        # self.ui.building
        # self.ui.building_2
        # self.ui.room

        self.ui.building.currentTextChanged.connect(self.configureRoomCombo)
        self.ui.room.currentTextChanged.connect(self.configureSensorCombo)

        # # list1 =[]
        # self.ui.connect_button.pressed.connect(self.connect)
        # # self.ui.connect_button.pressed.connect(self.get_host_with_port)
        # self.ui.connect_button.pressed.connect(self.change_profile_name)
        # # self.ui.connect_button.pressed.connect(self.disable_button)
        # self.ui.LogOut_button.pressed.connect(self.logout_button)
        # self.ui.Subscribe_button.pressed.connect(self.subscribe_button)
        # self.ui.UnSubscribe_button.pressed.connect(self.unsubscribe_button)
        # self.ui.UnBlock_button.pressed.connect(self.unblock_button)
        # self.ui.Block_button.pressed.connect(self.block_button)
        # self.ui.SendMessage_button.pressed.connect(self.send_message_button)
        # self.ui.Share_button.pressed.connect(self.share_twit_button)
        # self.ui.Pubkey_button.pressed.connect(self.pubkey_button)
        # self.ui.users_button.pressed.connect(self.users_button)
        # self.initializeIpPort()
        # self.initialize_button_conf()
        # self.initializeMyBlogsList()

    def findBuildingByName(self,bname):
        for b in self.buildings:
            if b.getName()==bname:
                return b
        return None



    def findRoomByName(self,building, rname):
        print("findRoomByName")
        try:
            for r in building.getRooms():
                if r.getName()==rname:
                    return r
        except:
            pass
        return None




    def configureRoomCombo(self):
        bname=self.ui.building.currentText()
        b=self.findBuildingByName(bname)
        self.currentBuilding=b

        if bname=="GSU":
            self.ui.myWindow.setPixmap(QtGui.QPixmap("./gsu.jpg"))
            self.ui.myLog.setText("LogDeneme")
            # pic.setGeometry(10, 10, 400, 100)
            # use full ABSOLUTE path to the image, not relative
            # pic.setPixmap(QtGui.QPixmap("./gsu.png"))
        elif bname=="INSA":
            self.ui.myWindow.setPixmap(QtGui.QPixmap("./insa.jpg"))
            self.ui.myLog.setText("LogDeneme")
            # pic.setGeometry(10, 10, 400, 100)
            # use full ABSOLUTE path to the image, not relative
            # pic.setPixmap(QtGui.QPixmap("./gsu.png"))
        else:
            self.ui.myWindow.setPixmap(QtGui.QPixmap("./bim.jpg"))
            self.ui.myLog.setText("LogDeneme")
            # pic.setGeometry(10, 10, 400, 100)
            # use full ABSOLUTE path to the image, not relative
            # pic.setPixmap(QtGui.QPixmap("./gsu.png"))

            self.ui.room.setDisabled(True)
            self.ui.sensor.setDisabled(True)

        if self.ui.room.currentText()=="None":
            self.ui.sensor.setDisabled(True)

        # print(b)
        if not bname=="None":
            self.setRooms(b)
        print("configureRoomCombo")
        pass

    def configureSensorCombo(self):
        if not self.ui.room.currentText()=="None":
            print("configureSensorCombo")
            rname=self.ui.room.currentText()
            print(rname,self.currentBuilding)
            r=self.findRoomByName(self.currentBuilding,rname)
            self.currentRoom=r
            self.setSensors(r)
        pass



    def setRooms(self,building):
        print("setRooms")
        self.ui.room.setDisabled(False)
        self.ui.room.clear()
        try:
            self.ui.room.addItem("None")
            for r in building.getRooms():
                self.ui.room.addItem(r.name)

        except:
            pass

    def setSensors(self,room):
        print("setSensors")
        self.ui.sensor.setDisabled(False)
        self.ui.sensor.clear()
        try:
            self.ui.sensor.addItem("None")
            for s in room.getSensors():
                self.ui.sensor.addItem(s.name)
        except:
            pass

    def initBuildings(self):
        self.ui.building.clear()
        self.ui.room.clear()
        self.ui.sensor.clear()
        self.ui.room.setDisabled(True)
        self.ui.sensor.setDisabled(True)

        self.ui.building.addItem("None")
        for b in self.buildings:
            self.ui.building.addItem(b.name)
            # self.initRooms(b)

        pass

    def run(self):
        self.initBuildings()
        self.show()
        self.qt_app.exec_()


def main():
    app = ProjectUi()
    app.run()

if __name__ == '__main__':
    main()