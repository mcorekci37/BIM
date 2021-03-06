
class Room:
    def __init__(self, name, id, floor, m2):
        self.name=name
        self.id=id
        self.floor=floor
        self.m2=m2
        self.sensors=list()

    def getName(self):
        return self.name
    def setName(self,name):
        self.name=name

    def getId(self):
        return self.id
    def setId(self,id):
        self.id=id

    def getFloor(self):
        return self.floor
    def setFloor(self,floor):
        self.floor=floor

    def getM2(self):
        return self.m2
    def setM2(self,m2):
        self.m2=m2

    def getSensors(self):
        return self.sensors

    def setSensors(self,sensors):
        self.sensors=sensors

    def addSensor(self,sensor):
        self.sensors.append(sensor)
    def removeSensor(self,sensor):
        self.sensors.remove(sensor)

    def __str__(self):
        s= "\t" +str(self.id) + ") " + self.name + "(" + str(self.floor) +". floor)"
        for sen in self.sensors:
            s+="\n\t"
            s+=str(sen)
        return s
