
from ExtractData import ExtractData
from PTP import PTP

if __name__ == '__main__':
    extractData = ExtractData("E:\\anul III\\AI\\date_proiect\\easy\PTP-RAND-1_4_2_16.json")
    problem_instance = PTP(extractData.getMaxWaitTime(), extractData.getPatients(), extractData.getLocations(),extractData.getVehicles())
    print(problem_instance.maxWaitTime)
    for car in problem_instance.getVehicles():
        print(car)
    for activity in problem_instance.getActivities():
        print(activity)
    matrix=extractData.getDistanceMatrix()
    print(matrix)
