
class Building:
    def __init__(self, name, id, address):
        self.name =name
        self.id =id
        self.address =address
        self.rooms =list()
        pass

    def getName(self):
        return self.name
    def setName(self ,name):
        self.name =name

    def getId(self):
        return self.id
    def setId(self ,id):
        self.id =id

    def getAddress(self):
        return self.address
    def setAddress(self ,address):
        self.address =address

    def getRooms(self):
        return self.rooms
    def setRooms(self ,rooms):
        self.rooms =rooms

    def findRoomByid(self,rid):
        for r in self.rooms:
            if r.id==rid:
                return r
        return None



    def addRoom(self ,room):
        self.rooms.append(room)
    def removeRoom(self ,room):
        self.rooms.remove(room)

    def __str__(self):
        s = "\t" +str(self.id) + ") " +self.name+"("+self.address+") | Rooms -->"
        for r in self.rooms:
            s+="\n\t"
            s+=str(r)
        return s
