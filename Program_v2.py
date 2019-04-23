import os
import time

# from arayuz_bim import Ui_MainWindow
from ui_v2 import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui, QtCore
from Building import Building
from Room import Room
from Sensor import Sensor
import threading
import sys
from PyQt5.QtWidgets import QApplication

SLEEPTIME_INSECONDS=0.5

class ProjectUi(QtWidgets.QMainWindow):
    def __init__(self,service):
        self.service = service
        self.currentBuilding=None
        self.currentRoom=None
        self.currentSensor=dict()
        self.currentSensor["Temperature"]=None
        self.currentSensor["Damp"]=None
        self.currentSensor["Co2"]=None
        self.currentSensor["Light"]=None
        self.currentSensor["Presence"]=None

        self.qt_app = QtWidgets.QApplication(sys.argv)
        QtWidgets.QWidget.__init__(self, None)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.building.currentTextChanged.connect(self.configureFloorCombo)
        self.ui.floor.currentTextChanged.connect(self.configureRoomCombo)
        self.ui.room.currentTextChanged.connect(self.configureSensorCombo)
        # self.ui.sensor.currentTextChanged.connect(self.configureButton)
        self.ui.streamButton.pressed.connect(self.startStreaming)

        self.sensorLogAssosication=dict()
        self.sensorLogAssosication["Temperature"]=self.ui.tempLog
        self.sensorLogAssosication["Damp"]=self.ui.dampLog
        self.sensorLogAssosication["Co2"]=self.ui.co2Log
        self.sensorLogAssosication["Light"]=self.ui.lightLog
        self.sensorLogAssosication["Presence"]=self.ui.presenceLog


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
        for b in self.service.buildings:
            if b.getName()==bname:
                return b
        return None



    def configureFloorCombo(self):
        print("configureFloorCombo")
        bname=self.ui.building.currentText()
        b=self.service.findBuildingByName(bname)
        self.currentBuilding=b

        if bname=="GSU":
            self.ui.myWindow.setPixmap(QtGui.QPixmap("./floor_sized.jpg"))
            self.ui.myLog.setText("Galatasaray University")
        elif bname=="INSA":
            self.ui.myWindow.setPixmap(QtGui.QPixmap("./insa_sized.jpg"))
            self.ui.myLog.setText("INSA Lyon | Institut National des Sciences Appliquées de Lyon")
        else:
            self.ui.myWindow.setPixmap(QtGui.QPixmap("./bim_sized.jpg"))
            self.ui.myLog.setText("Thanks for using Building Information Modeling Application")

        self.setFloors(b)
        # self.setRooms(b)

    def configureRoomCombo(self):
        print("configureRoomCombo")
        bname=self.ui.building.currentText()
        b=self.service.findBuildingByName(bname)
        self.currentBuilding=b

        # if bname=="GSU":
        #     self.ui.myWindow.setPixmap(QtGui.QPixmap("./gsu_sized.jpg"))
        #     self.ui.myLog.setText("Galatasaray University")
        # elif bname=="INSA":
        #     self.ui.myWindow.setPixmap(QtGui.QPixmap("./insa_sized.jpg"))
        #     self.ui.myLog.setText("INSA Lyon | Institut National des Sciences Appliquées de Lyon")
        # else:
        #     self.ui.myWindow.setPixmap(QtGui.QPixmap("./bim_sized.jpg"))
        #     self.ui.myLog.setText("Thanks for using Building Information Modeling Application")

        # self.setFloors(b)
        if not self.ui.floor.currentText()=="None":
            self.setRooms(b)

    def setFloors(self,building):
        # self.setRooms(building)
        print("setFloors")
        # self.ui.room.setDisabled(False)
        self.ui.floor.clear()
        if not building is None:
            # self.ui.room.addItem("None")
            self.ui.floor.addItem("None")
            self.ui.floor.addItem("First Floor")
            self.ui.floor.addItem("Second Floor")
            self.ui.floor.setDisabled(False)
        else:#if building value is None
            self.ui.floor.setDisabled(True)
            self.ui.temperature.setVisible(False)
            self.ui.damp.setVisible(False)
            self.ui.co2.setVisible(False)
            self.ui.light.setVisible(False)
            self.ui.presence.setVisible(False)
            # self.ui.sensor.setDisabled(True)
            pass

    def configureSensorCombo(self):
        print("configureSensorCombo")
        rname=self.ui.room.currentText()
        r=self.service.findRoomByName(self.currentBuilding,rname)
        self.currentRoom=r
        self.setSensors(r)



    def setRooms(self,building):
        print("setRooms")
        # self.ui.room.setDisabled(False)
        self.ui.room.clear()
        if not self.ui.floor.currentText()==None:
            try:
                self.ui.room.addItem("None")
                for r in building.getRooms():
                    self.ui.room.addItem(r.name)
                self.ui.room.setDisabled(False)
            except:#if building value is None
                self.ui.room.setDisabled(True)
                self.ui.temperature.setVisible(False)
                self.ui.damp.setVisible(False)
                self.ui.co2.setVisible(False)
                self.ui.light.setVisible(False)
                self.ui.presence.setVisible(False)
                # self.ui.sensor.setDisabled(True)

    def setSensors(self,room):
        print("setSensors")
        # self.ui.sensor.setDisabled(False)
        # self.ui.sensor.clear()
        try:
            # self.ui.sensor.addItem("None")
            for s in room.getSensors():
                # self.ui.sensor.addItem(s.name)
                if s.getName()=="Temperature":
                    self.ui.temperature.setVisible(True)
                if s.getName()=="Damp":
                    self.ui.damp.setVisible(True)
                if s.getName()=="Co2":
                    self.ui.co2.setVisible(True)
                if s.getName()=="Light":
                    self.ui.light.setVisible(True)
                if s.getName() == "Presence":
                    self.ui.presence.setVisible(True)
        except:#if room value is None
            self.ui.temperature.setVisible(False)
            self.ui.damp.setVisible(False)
            self.ui.co2.setVisible(False)
            self.ui.light.setVisible(False)
            self.ui.presence.setVisible(False)
            pass

    def initBuildings(self):
        self.ui.building.clear()
        self.ui.room.clear()
        self.ui.floor.clear()
        # self.ui.sensor.clear()
        self.ui.floor.setDisabled(True)
        self.ui.room.setDisabled(True)
        self.ui.temperature.setVisible(False)
        self.ui.damp.setVisible(False)
        self.ui.co2.setVisible(False)
        self.ui.light.setVisible(False)
        self.ui.presence.setVisible(False)

        self.ui.building.addItem("None")
        self.ui.floor.addItem("None")
        self.ui.room.addItem("None")
        for b in self.service.buildings:
            self.ui.building.addItem(b.name)
            # self.initRooms(b)

        pass

    def configureButton(self):
        print("configureButton")
        # sname=self.ui.sensor.currentText()
        temperatureStat=self.ui.temperature.isChecked()
        dampStat=self.ui.temperature.isChecked()
        co2Stat=self.ui.temperature.isChecked()
        lightStat=self.ui.temperature.isChecked()
        presenceStat=self.ui.temperature.isChecked()

        for k in self.currentSensor.keys():
            if self.currentSensor[k].isChecked():
                pass

        try:
            if temperatureStat:
                self.service.findSensorByName(self.currentBuilding,self.currentRoom,"Temperature")
                self.currentSensor["Temperature"] = True
            if dampStat:
                self.service.findSensorByName(self.currentBuilding,self.currentRoom,"Damp")
                self.currentSensor["Damp"] = True
            if co2Stat:
                self.service.findSensorByName(self.currentBuilding,self.currentRoom,"Co2")
                self.currentSensor["Co2"] = True
            if lightStat:
                self.service.findSensorByName(self.currentBuilding,self.currentRoom,"Light")
                self.currentSensor["Light"] = True
            if presenceStat:
                self.service.findSensorByName(self.currentBuilding,self.currentRoom,"Presence"),
                self.currentSensor["Presence"] = True


            # s=self.service.findSensorByName(self.currentBuilding,self.currentRoom.getName(),sname)
            # self.currentSensor = s
        except:
            pass
        # self.setButton(s)

    def startStreaming(self):
        # print(self.currentSensor.last1000values)
        # self.ui.myLog.setText(str(self.currentSensor.last1000values)

        # sys.stdout = Unbuffered(sys.stdout)
        if self.ui.temperature.isChecked():
            tempS=self.service.findSensorByName(self.currentBuilding,self.currentRoom.getName(),"Temperature")
            self.currentSensor["Temperature"]=tempS
        else:
            self.currentSensor["Temperature"]=None
        if self.ui.damp.isChecked():
            tempS=self.service.findSensorByName(self.currentBuilding,self.currentRoom.getName(),"Damp")
            self.currentSensor["Damp"]=tempS
        else:
            self.currentSensor["Damp"]=None
        if self.ui.co2.isChecked():
            tempS=self.service.findSensorByName(self.currentBuilding,self.currentRoom.getName(),"Co2")
            self.currentSensor["Co2"] = tempS
        else:
            self.currentSensor["Co2"] = tempS
        if self.ui.light.isChecked():
            tempS=self.service.findSensorByName(self.currentBuilding,self.currentRoom.getName(),"Light")
            self.currentSensor["Light"]=tempS
        else:
            self.currentSensor["Light"]=tempS
        if self.ui.presence.isChecked():
            tempS=self.service.findSensorByName(self.currentBuilding,self.currentRoom.getName(),"Presence")
            self.currentSensor["Presence"]=tempS
        else:
            self.currentSensor["Presence"]=tempS

        QApplication.processEvents()
        for i in  range(len(self.currentSensor["Temperature"].last1000values)):
            # self.ui.myLog.setText(self.ui.myLog.toPlainText() + " >> " +  self.currentSensor.last1000values[i] )
            QApplication.processEvents()

            for k in self.currentSensor.keys():
                if not self.currentSensor[k]==None:
                    self.sensorLogAssosication[k].append("> " +  self.currentSensor[k].last1000values[i] )

            # self.ui.tempLog.append("> " +  self.currentSensor["Temperature"].last1000values[i] )
            # self.ui.dampLog.append("> " +  self.currentSensor["Damp"].last1000values[i][:4] )
            # self.ui.co2Log.append("> " +  self.currentSensor["Co2"].last1000values[i] )
            # self.ui.lightLog.append("> " +  self.currentSensor["Light"].last1000values[i] )
            # self.ui.presenceLog.append("> " +  self.currentSensor["Presence"].last1000values[i] )

            time.sleep(SLEEPTIME_INSECONDS)

        # for i in self.currentSensor.last1000values:
        #     self.ui.myLog.setText(self.ui.myLog.toPlainText() + " >> " +  i )
        #     # time.sleep(0.01)

        # st=StreamThread(self.ui,self.currentSensor)
        # st.start()
        # st.join()

    def run(self):
        self.initBuildings()
        self.show()
        self.qt_app.exec_()






class StreamThread(threading.Thread):
    def __init__(self, ui,sensor):
        threading.Thread.__init__(self)
        self.ui = ui
        self.sensor=sensor

    def run(self):
        for i in self.sensor.last1000values:
            self.ui.myLog.setText(self.ui.myLog.toPlainText() + " >> " +  i )
            # time.sleep(00.1)



class Service:

    def __init__(self):
        self.buildings=list()
        self.nbBuilding=0
        self.nbRoom=0
        self.nbSensor=0
        self.database=dict()

    def createBuilding(self,name,address):
        self.nbBuilding+=1
        b=Building(name,self.nbBuilding,address)
        self.buildings.append(b)

    def findBuildingByid(self,bid):
        for b in self.buildings:
            if b.id==bid:
                return b
        return None

    def findBuildingByName(self,bname):
        for b in self.buildings:
            if b.getName()==bname:
                return b
        return None

    def printBuildings(self):
        for b in self.buildings:
            print(b)
        return len(self.buildings)

    def chooseBuilding(self):
        lenB=self.printBuildings()
        while(True):
            choice=int(input("Which on of the building do you want to choose --> "))
            if int(choice)<=lenB:
                break
        b=self.findBuildingByid(self.buildings[choice-1].getId())
        return b

    def initBuildings(self):
        self.createBuilding("GSU", "Ortaköy, 34200")
        self.createBuilding("INSA", "LYON")
        self.initRooms()



    def createRoom(self,buildingId, name,floor,m2):
        self.nbRoom+=1
        r=Room(name,self.nbRoom,floor,m2)
        self.findBuildingByid(buildingId).addRoom(r)
        return r;

    def initRooms(self):
        r=self.createRoom(1, "Mr. T. Askali", 1, 15)
        self.createSensorsForRoom(r)
        r=self.createRoom(1, "Mr. O. Pinarer", 1, 15)
        self.createSensorsForRoom(r)
        r=self.createRoom(1, "Mrs. S. Turhan", 1, 15)
        self.createSensorsForRoom(r)
        r=self.createRoom(2, "Mr. O. Pinarer", 2, 20)
        self.createSensorsForRoom(r)
        r=self.createRoom(2, "Mr. Y. Gripay", 2, 20)
        self.createSensorsForRoom(r)
        r=self.createRoom(2, "Mrs. S. Servigne", 2, 20)
        self.createSensorsForRoom(r)


    def findRoomByName(self,building, rname):
        print("findRoomByName")
        try:
            for r in building.getRooms():
                if r.getName()==rname:
                    return r
        except:
            pass
        return None

    def findSensorByKind(self,building, rname, skind):
        print("findSensorByKind")
        try:
            for s in ( self.findRoomByName(building,rname) ).getSensors():
                if s.getKind()==skind:
                    return s
        except:
            pass
        return None

    def findSensorByName(self,building, rname, sname):
        print("findSensorByName")
        try:
            r=self.findRoomByName(building,rname)
            for s in r.getSensors():
                if s.getName()==sname:
                    return s
        except:
            pass
        return None



    def createSensorsForRoom(self,room):
        # if sensorId starts with 100 that means its type is Temperature
        # 200 that means its type is humidité
        # 300 that means its type is émission de CO2
        # 400 that means its type is luminosité
        # 500 that means its type is présence

        s=Sensor("Temperature",1001,"temperature")
        self.initValuesForSensor("temperature",s)
        room.addSensor(s)

        s=Sensor("Damp",2001,"damp")
        self.initValuesForSensor("damp",s)
        room.addSensor(s)

        s=Sensor("Co2",3001,"co2")
        self.initValuesForSensor("co2",s)
        room.addSensor(s)

        s=Sensor("Light",4001,"light")
        self.initValuesForSensor("light",s)
        room.addSensor(s)

        s=Sensor("Presence",5001,"presence")
        self.initValuesForSensor("presence",s)
        room.addSensor(s)

        return room

    def initValuesForSensor(self,kind,sensor):
        sensor.last1000values=self.database[kind]

    def initDatabase(self):
        tempFile=open("./data/temperature.txt","r")
        line=tempFile.readline()
        l=line.split(",")
        self.database["temperature"]=l

        tempFile=open("./data/damp.txt","r")
        line=tempFile.readline()
        l=line.split(",")
        self.database["damp"]=l

        tempFile=open("./data/co2.txt","r")
        line=tempFile.readline()
        l=line.split(",")
        self.database["co2"]=l

        tempFile=open("./data/light.txt","r")
        line=tempFile.readline()
        # l= list(map(int,line.split(",")))
        l=line.split(",")
        self.database["light"]=l

        tempFile=open("./data/presence.txt","r")
        line=tempFile.readline()
        l=line.split(",")
        self.database["presence"]=l

        pass

class ArayuzThread(threading.Thread):
    def __init__(self, threadname,service):
        threading.Thread.__init__(self)
        self.threadName = threadname
        self.service=service

    def run(self):
        app = ProjectUi(self.service)
        app.run()


def main():


    service = Service()
    service.initDatabase()
    service.initBuildings()
    app = ProjectUi(service)
    app.run()

    # arayuzT = ArayuzThread("Arayüz Thread",service)
    # arayuzT.start()
    # arayuzT.join()

if __name__ == '__main__':
    main()