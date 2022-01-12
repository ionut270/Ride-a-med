from ExtractData import ExtractData
from PTP import PTP
def getHoursMinutes(time:str):
    hours=time.split("h")
    minutes=hours[1].split("m")
    return int(hours[0]),int(minutes[0])
def compareTime(time1,time2):
    """-1-daca t1 mai mic decat t2
        0-daca sunt egale
        1-t1>t2

    """
    h_m1 = getHoursMinutes(time1)
    h_m2 = getHoursMinutes(time2)
    if h_m1[0]==h_m2[0] and h_m1[1]==h_m2[1]:
        return 0
    if h_m1[0]<h_m2[0]:
        return -1
    elif h_m1[1]<h_m2[1] and h_m1[0]==h_m2[0]:
        return -1
    else:
        return 1

print(compareTime("6h9m","7h5m"))


def getMinimumIndex(list_of_strings):
    index=0
    minim=list_of_strings[0]
    for i in range(1,len(list_of_strings)):
        if compareTime(list_of_strings[i],minim)==-1:
            index=i
            minim=list_of_strings[i]
    return index

print(getMinimumIndex(['6h9m', '7h1m', '3h5m', '7h19m']))
# extractData = ExtractData("E:\\anul III\\AI\\date_proiect\\easy\PTP-RAND-1_4_2_16.json")
# problem_instance = PTP(extractData.getMaxWaitTime(), extractData.getPatients(), extractData.getLocations(),
#                        extractData.getVehicles())
# activities=problem_instance.getActivities()
# print (len(activities))
# activities.sort(key=lambda x:x.getStartDate())
# for a in activities:
#     print(a.getID(),a.getType(),a.getStartDate())