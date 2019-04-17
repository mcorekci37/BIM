import Building
from Building import Building
from Room import Room
from Sensor import Sensor
import Sensor
class Service:

    def __init__(self):
        self.buildings=list()
        self.nbBuilding=0
        self.nbRoom=0


    def createBuilding(self,name,address):
        self.nbBuilding+=1
        b=Building(name,self.nbBuilding,address)
        self.buildings.append(b)

    def findBuildingByid(self,bid):
        for b in self.buildings:
            if b.id==bid:
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



    def createRoom(self,buildingId, name,floor,m2):
        self.nbRoom+=1
        r=Room(name,self.nbRoom,floor,m2)
        self.findBuildingByid(buildingId).addRoom(r)



    def initRooms(self):
        self.createRoom(1, "Mr. Pinarer", 1, 15)
        pass

    def createSensorsForRoom(self,room):
        # if sensorId starts with 100 that means its type is Temperature
        # 200 that means its type is humidité
        # 300 that means its type is émission de CO2
        # 400 that means its type is luminosité
        # 500 that means its type is présence

        s=Sensor("Temperature",1001,"Temperature")
        room.addSensor(s)
        s=Sensor("Humidité",2001,"Humidité")
        room.addSensor(s)
        s=Sensor("Emission de CO2",3001,"Emission de CO2")
        room.addSensor(s)
        s=Sensor("Luminosité",4001,"Luminosité")
        room.addSensor(s)
        s=Sensor("Présence",5001,"Présence")
        room.addSensor(s)

        return room

def main():
    service = Service()
    service.initBuildings()
    service.initRooms()

    b=service.chooseBuilding()
    print ("Your choice: ")
    print (b)
    # print(service.buildings[0])


if __name__ == '__main__':
    main()