class Patient:
    def __init__(self,id, category, load, start_location,destination, end_location, rdvTime, rdvDuration, srvDuration):
        self.id=id
        self.category = category
        self.load = load
        self.start_location = start_location
        self.destination=destination
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
    def getId(self):
        return self.id
    def getDestination(self):
        return self.destination

    def __str__(self):
        out=f"Pacient id : {self.id} \n category: {self.category} \n places_neede: {self.load} \n " \
            f"start:{self.start_location}\n destinatino:{self.destination} \n" \
            f"end: {self.end_location} \n Begin appointment time:{self.rdvTime} \n" \
            f"treatment duration{self.rdvDuration}\n embark\debark: {self.srvDuration} \n"
        return  out