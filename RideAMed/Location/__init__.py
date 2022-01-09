class Location:
    def __init__(self,id, lat, long, category):
        self.id=id
        self.lat = lat
        self.long = long
        self.category = category
    def getId(self):
        return self.id
    def getLat(self):
        return self.lat

    def getLong(self):
        return self.long

    def getCategory(self):
        return self.category
    def __str__(self):
        return f"({self.id},{self.category})"

    def __repr__(self):
        return str(self)