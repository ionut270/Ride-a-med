import json
from Vehicle import Vehicle
from Patient import Patient
from Location import Location


class ExtractData:
    def __init__(self, json_file):
        self.json_file = json_file
        self.vehicles = []
        self.locations = []
        self.patients = []
        self.distance_matrix = [[]]
        self.maxWaitTime = 0
        self.extractMatrixDistances()
        self.extractPatients()
        self.extractVehicles()
        self.extractLocations()
        self.extractMaxWaitTime()

    def getMaxWaitTime(self):
        return self.maxWaitTime

    def getDistanceMatrix(self):
        return self.distance_matrix

    def getVehicles(self):
        return self.vehicles

    def getLocations(self):
        return self.locations

    def getPatients(self):
        return self.patients

    def extractVehicles(self):
        file_descriptor = open(self.json_file)
        data = json.load(file_descriptor)
        vehicles = []
        for vehicle_data in data["vehicles"]:
            vehicles.append(Vehicle(vehicle_data["canTake"],
                                    vehicle_data["start"],
                                    vehicle_data["end"],
                                    vehicle_data["capacity"],
                                    vehicle_data["availability"]))
        self.vehicles = vehicles
        file_descriptor.close()

    def extractPatients(self):
        file_descriptor = open(self.json_file)
        data = json.load(file_descriptor)
        patients = []
        for patient_data in data["patients"]:
            patients.append(Patient(patient_data["category"],
                                    patient_data["load"],
                                    patient_data["start"],
                                    patient_data["end"],
                                    patient_data["rdvTime"] + 'm',
                                    patient_data["rdvDuration"] + 'm',
                                    patient_data["srvDuration"] + 'm'))
        self.patients = patients
        file_descriptor.close()

    def extractLocations(self):
        file_descriptor = open(self.json_file)
        data = json.load(file_descriptor)
        places = []
        for place_data in data["places"]:
            places.append(Location(place_data["lat"],
                                   place_data["long"],
                                   place_data["category"]))
        self.locations = places
        file_descriptor.close()

    def extractMatrixDistances(self):
        file_descriptor = open(self.json_file)
        data = json.load(file_descriptor)
        self.distance_matrix = data["distMatrix"]
        file_descriptor.close()

    def extractMaxWaitTime(self):
        file_descriptor = open(self.json_file)
        data = json.load(file_descriptor)
        self.maxWaitTime = data["maxWaitTime"]
        file_descriptor.close()
