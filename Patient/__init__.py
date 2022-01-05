class Patient:
    def __init__(self, category, load, start_location, end_location, rdvTime, rdvDuration, srvDuration):
        self.category = category
        self.load = load
        self.start_location = start_location
        self.end_location = end_location
        self.rdvTime = rdvTime
        self.rdvDuration = rdvDuration
        self.srvDuration = srvDuration
        self.selected = False

    def setSelected(self,value):
        self.selected = value

    def getIsSelected(self):
        return self.selected

    def getCategory(self):
        return self.category

    def getLoad(self):
        return self.load

    def getStartLocation(self):
        return self.start_location

    def getEndLocation(self):
        return self.end_location

    def getRdvTime(self):
        return self.rdvTime

    def getRdvDuration(self):
        return self.rdvDuration

    def getSrvDuration(self):
        return self.srvDuration
