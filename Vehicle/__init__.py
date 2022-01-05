

class Vehicle:
    def __init__(self, categories, start_depot, end_depot, capacity, availability):
        self.categories = categories
        self.start_depot = start_depot
        self.end_depot = end_depot
        self.capacity = capacity
        self.availability = availability

    def getCategories(self):
        return self.categories

    def getStart_depot(self):
        return self.start_depot

    def getEnd_depot(self):
        return self.end_depot

    def getCapacity(self):
        return self.capacity

    def getAvailability(self):
        return self.availability

