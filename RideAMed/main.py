
from ExtractData import ExtractData
from PTP import PTP

if __name__ == '__main__':
    extractData = ExtractData("C:\\Users\\oance\\Desktop\\Ride-a-med\\RideAMed\\easy\\easy\\PTP-RAND-2_12_5_48.json")
    problem_instance = PTP(extractData.getMaxWaitTime(), extractData.getPatients(), extractData.getLocations(),extractData.getVehicles())
    print(problem_instance.maxWaitTime)
    for car in problem_instance.getVehicles():
        print(car)
    for activity in problem_instance.getActivities():
        print(activity)
    matrix=extractData.getDistanceMatrix()
    print(matrix)
