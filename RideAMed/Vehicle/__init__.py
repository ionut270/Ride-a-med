

class Vehicle:
    def __init__(self,id, categories, start_depot, end_depot, capacity, availability):
        self.id=id
        self.categories = categories
        self.start_depot = start_depot
        self.end_depot = end_depot
        self.capacity = capacity
        self.availability = availability

    def getCategories(self):
        return self.categories

    def getStartDepo(self):
        return self.start_depot

    def getEndDepo(self):
        return self.end_depot
    def getId(self):
        return self.id
    def getCapacity(self):
        return self.capacity
    def getStartTime(self):
        print(type(self.availability))
        hours=self.availability[0].split(":")
        return hours[0]
    def getEndTime(self):
        print(type(self.availability))
        hours = self.availability[0].split(":")
        return hours[1]
    def getAvailability(self):
        return self.availability
    def __str__(self):
        return f" id : {self.id} \n category: {self.categories} \n " \
               f"start-depo: {self.start_depot} \n " \
               f"end-depo:{self.end_depot}\n " \
               f"capacity:{self.capacity} \n" \
               f"availability: {self.availability} \n"
