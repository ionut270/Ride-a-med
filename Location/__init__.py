class Location:
    def __init__(self, lat, long, category):
        self.lat = lat
        self.long = long
        self.category = category

    def getLat(self):
        return self.lat

    def getLong(self):
        return self.long

    def getCategory(self):
        return self.category
