
class Building:
    def __init__(self, name, id, address):
        self.nam e =name
        self.i d =id
        self.addres s =address
        self.room s =list()
        pass

    def getName(self):
        return self.name
    def setName(self ,name):
        self.nam e =name

    def getId(self):
        return self.id
    def setId(self ,id):
        self.i d =id

    def getAddress(self):
        return self.address
    def setAddress(self ,address):
        self.addres s =address

    def getRooms(self):
        return self.rooms
    def setRooms(self ,rooms):
        self.room s =rooms

    def addRoom(self ,room):
        self.rooms.append(room)
    def removeRoom(self ,room):
        self.rooms.remove(room)
