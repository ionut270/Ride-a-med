from Patient import Patient
from ExtractData import ExtractData
from PTP import PTP
from Activity import TypeActivity
MAX_WAIT_TIME="00h30m"
from timeCalculator import subtractTime,addTime
def sortByMedCenter(pacients_list: list, med_centers: list):
    sorted_pacients = []
    for i in range(len(med_centers)):
        sorted_pacients.append([])
    for pacient in pacients_list:
        sorted_pacients[pacient.getDestination()].append(pacient)
    return sorted_pacients


def sortPacientsForEveryMedByArrivingTime(list_of_lists_of_pacients: list):
    for l in list_of_lists_of_pacients:
        l.sort(key=lambda x: x.getRdvTime())
    return list_of_lists_of_pacients
def sortPacientsBytimeWhenTheyNeedToBePicked(list_of_pacients:list):
    list_of_pacients.sort(key=lambda x: subtractTime(x.getRdvTime(),MAX_WAIT_TIME))
    return list_of_pacients
def getMedCEnters(locations: list):
    med_centers = [location for location in locations if location.getCategory() == 0]
    return med_centers
def getDepos(locations: list):
    depos = [location for location in locations if location.getCategory() == 1]
    return depos
def getPacientLocations(patients:list):
    return[(p.getStartLocation(),p.getId()) for p in patients]

def minimumOfVectro(vector: int, nodepo: list):
    min = 10_0000
    for i in range(0, len(vector)):
        if i not in nodepo:
            if vector[i] != 0 and vector[i] < min:
                min = vector[i]
                index = i
    return index, min


def getMinimumFromLocationToOther(spefic_location: int, distance_matrix: int):
    vector = distance_matrix[spefic_location]
    print(vector)
    return minimumOfVectro(vector)


def getMinimumFromLocationToOther2(spefic_location: int, distance_matrix: int, nodepo: list):
    """nodepo-lista cu indecsii depourilor"""
    """to do first_time=true sa nu ia in considerare si centrele medicale"""
    vector = distance_matrix[spefic_location]
    print(vector)
    return minimumOfVectro(vector, nodepo)


def getDestinationsOfPatients(patients_list):
    return [(patient.getId(), patient.getDestination(), patient.getStartLocation(), patient.getEndLocation()) for
            patient in patients_list]


def getPacientWithID(start_location: int, patients_list: list):
    for p in patients_list:
        if p.getStartLocation() == start_location:
            return p

def getForwardActivities(activities:list):
    return [ac for ac in activities if ac.getType() == TypeActivity.FORWARD]
def getBackwardActivities(activities:list):
    return [ac for ac in activities if ac.getType() == TypeActivity.BACKWARD]
# extractData = ExtractData("E:\\anul III\\AI\\date_proiect\\easy\PTP-RAND-1_4_2_16.json")
# problem_instance = PTP(extractData.getMaxWaitTime(), extractData.getPatients(), extractData.getLocations(),
#                        extractData.getVehicles())
# locations = problem_instance.getLocations()
# patients = problem_instance.getPatients()
# med_centers = getMedCEnters(locations)
# depos = getDepos(locations)
# depos_indexes = [dep.getId() for dep in depos]
# print("depos:", depos_indexes)
# dmatrix = extractData.getDistanceMatrix()
# print(len(med_centers))
# lists = sortByMedCenter(patients, med_centers)
# print("obs line")
# l1 = sortPacientsForEveryMedByArrivingTime(lists)
# for l in l1:
#     print("newList")
#     for p in l:
#         print(p.getStartLocation())
# var1 = getMinimumFromLocationToOther2(4, dmatrix, depos_indexes)
# result = getDestinationsOfPatients(patients)
# for r in result:
#     print(r)
# p = getPacientWithID(getMinimumFromLocationToOther2(4, dmatrix, depos_indexes)[0], patients)
# print(p)
# print(var1[0], dmatrix[var1[0]][p.getDestination()])
# print(getMinimumFromLocationToOther2(4, dmatrix, depos_indexes))
# print(getMinimumFromLocationToOther2(10, dmatrix, depos_indexes))
# print(dmatrix[3][2])
# p2 = getPacientWithID(15, patients)
# p3 = getPacientWithID(10, patients)
# print(p2, p3)
# def transformToHoursMiunutes(seconds):
#     m, s = divmod(seconds, 60)
#     h, m = divmod(m, 60)
#     return f"{h}h{m}m"
# activities=problem_instance.getActivities()
# print(len(activities))
# forActivities=[ac for ac in activities if ac.getType()==TypeActivity.FORWARD]
# forActivities.sort(key=lambda x:x.getStartDate())
# for a in forActivities:
#     print(transformToHoursMiunutes(a.getStartDate()),a.getPatient().getId())
#     #print(a.getStartDate(),a.getSrvDuration(),a.getEndDate())
# lp=sortPacientsBytimeWhenTheyNeedToBePicked(patients)
# for p in lp:
#     print(subtractTime(p.getRdvTime(),MAX_WAIT_TIME))
