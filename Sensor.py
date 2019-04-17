
class Sensor:
    def __init__(self, name, id, kind):
        self.name=name
        self.id=id
        self.kind=kind
        self.value=None
        # self.last100values=Queue.Queue()
        self.last100values=list()
        pass

    def getName(self):
        return self.name
    def setName(self,name):
        self.name=name

    def getId(self):
        return self.id
    def setId(self,id):
        self.id=id

    def getKind(self):
        return self.kind
    def setKind(self,kind):
        self.kind=kind

    def getValue(self):
        return self.value
    def setValue(self,value):
        self.value=value
        self.last100values.insert(0,value)
        if len(self.last100values)>=100:
            self.last100values.remove(len(self.last100values)-1)
        # self.last100values.put(value)
        # if len(self.last100values)>=100:
        #     self.last100values.get()

    def getValue(self):
        return self.value
    def setValue(self,value):
        self.value=value
