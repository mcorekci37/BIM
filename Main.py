import Building
from Building import Building
from Room import Room
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


    def createRoom(self,buildingId, name,floor,m2):
        self.nbRoom+=1
        r=Room(name,self.nbRoom,floor,m2)
        self.findBuildingByid(buildingId).addRoom(r)

    def chooseBuilding(self):
        self.printBuildings()

    def printBuildings(self):
        for b in self.buildings:
            print(b)
        return len(self.buildings)

    def initBuildings(self):
        self.createBuilding("GSU", "Ortaköy, 34200")
        self.createBuilding("INSA", "LYON")

    def initRooms(self):
        pass

def main():
    service = Service()
    service.initBuildings()
    service.chooseBuilding()

    service.createRoom(1,"Mr. Pinarer", 1, 15)
    print(service.buildings[0])

if __name__ == '__main__':
    main()