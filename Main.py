import Building
from Building import Building
import Sensor
class Service:
    def __init__(self):
        self.buildings=list()

    def createBuilding(self,name,address):
        b=Building(name,address)
        self.buildings.append(b)

    def chooseBuilding(self):
        self.printBuildings()
        pass

    def printBuildings(self):
        i=1
        for b in self.buildings:
            print(i," )",b.name,"(",b.address,")")
            i+=1
        return len(self.buildings)

def main():
    service = Service()
    service.createBuilding("GSU","Ortaköy, 34200")
    service.chooseBuilding()
    pass

if __name__ == '__main__':
    main()