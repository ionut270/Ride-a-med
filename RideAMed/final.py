from Activity import Activity
from ExtractData import ExtractData
from PTP import PTP
from monitor import Monitor
from timeCalculator import convertFromSecondsToHM, compareTime


def loadPacientInCar(car_monitor: Monitor, activity: Activity, matrix, load_flag):
    car_monitor.addActivityToCar(activity)
    car_monitor.updateCarCapacity(load_flag)
    new_pozition = activity.getPatient().getStartLocation()
    car_monitor.updateCurrentTime(matrix[car_monitor.getCurrentPosition()][new_pozition])
    car_monitor.setNewPosition(new_pozition)


def getNeareasrtCar(monitors: list, activity: Activity, matrix: int):
    minim = 10000
    save_monitor = None
    for m in monitors:
        new_patient_position = activity.getPatient().getStartLocation()
        distance = matrix[m.getCurrentPosition()][new_patient_position]
        if distance < minim:
            minim = distance
            save_monitor = m
    return save_monitor


def checkCarLoad(car_monitor: Monitor, activity: Activity):
    if car_monitor.getCurrentCarCapacity() - activity.getPatient().getLoad() < 0:  # verific daca luand acel pacient depasesc capacitatea masinii
        return 0
    return 1

def verifyTimes(car_monitor:Monitor,activity:Activity):
    remainingTimes=car_monitor.RemaninigTime():
    #o sa o fac eu maine asta
def findAvailableCar(monitors: list, activity: Activity, matrix: int):
    car_monitor = getNeareasrtCar(monitors, activity, matrix)
    if checkCarLoad(car_monitor, activity) == 1:
        return car_monitor
    else:
        for m in monitors:  # daca cea mai apropiata masina nu e disponibila caut alta masina disponibila
            #if m.getCar().getId() != car_monitor.getCar().getId():
                if checkCarLoad(m, activity) == 1:  # !!!!!!!!!!!!!! de facut in acelasi timp si check cu remainig_times
                    # !!!!!!!!!!!!!! daca pacientul pe care vreau sa-l iau pune in dificultate trasnportarea celorlalti nu-l iau
                    return m
                else:  # daca nu am nicio masina disponibila
                    car_monitor = None
    return car_monitor


def getMinimumIndex(list_of_strings):
    index = 0
    minim = list_of_strings[0]
    for i in range(1, len(list_of_strings)):
        if compareTime(list_of_strings[i], minim) == -1:
            index = i
            minim = list_of_strings[i]
    return index


####
def unloadCars(monitor_list: list, matrix: int):
    for m in monitor_list:
        car_activities_list=m.getCarActivities()
        remaining_times= m.getRemainingTime()
        index = getMinimumIndex(remaining_times)
        activity = car_activities_list[index]
        print(f"Pacient with id {activity.getPatient().getId()} on destination", activity.getID(), activity.getType())
        updateAfterUnload(m, activity, matrix)


def updateAfterUnload(car_monitor: Monitor, activity: Activity, matrix: int):
    if activity.getType() == 1:
        car_monitor.succesfull_close_activities_forward.append(activity)
    else:
        car_monitor.succesfull_close_activities_backward.append(activity)
        # de facut check cu timpul activitatii
    patient = activity.getPatient()
    car_monitor.updateCarCapacity(patient.getLoad(), False)
    ########!!!!!!!!de facut
    #pentru backward new_poz=(activity.getPatient().getEndLocation)
    new_pozition = activity.getPatient().getDestination()  # mut masina la destinatia pacientului
    car_monitor.updateCurrentTime(matrix[car_monitor.getCurrentPosition()][new_pozition])
    car_monitor.setNewPosition(new_pozition)
    car_monitor.removeActivity(activity)


def printActivities(activities: list):
    for ac in activities:
        if ac.getType() == 1:
            print("F", ac.getID(), convertFromSecondsToHM(ac.getStartDate()), convertFromSecondsToHM(ac.getEndDate()))
        else:
            print("B", ac.getID(), convertFromSecondsToHM(ac.getStartDate()), convertFromSecondsToHM(ac.getEndDate()))


def checkIfValidActivity(activy: Activity,car_monitor: Monitor):  # aici car_monitor nu coanteaza pentru ca accesez lista de clasa
    if activy.getType() == 0:  # activitea e backward trebuie sa verific daca cea forward cu acelasi id s-a realizat cu succes si timpul curent al masinii sa si aprox cu cel de start.
        forward_done_activities = [a.getID() for a in car_monitor.succesfull_close_activities_forward]
        if activy.getID() not in forward_done_activities:  # or activity.StartTime()-car.getCurrentTime()<5min
            return 0
        else:
            return 1
    else:
        return 2


def findCarThatHasForwardActivity(monitors_list: list, activity_id: int, matrix: int):
    for m in monitors_list:
        for ac in m.getCarActivities():
            if ac.getID() == activity_id:
                activ = ac
                car = m
    updateAfterUnload(car, activ, matrix)

def getTotalofActivitiesDone(list_of_forwardActivities,list_of_backward_activities):
    count=0
    for ac in list_of_forwardActivities:
        for bc in list_of_backward_activities:
            if ac.getID()==bc.getID():
                count+=1
    return count

def main():
    extractData = ExtractData("E:\\anul III\\AI\\date_proiect\\easy\PTP-RAND-1_4_2_16.json")
    problem_instance = PTP(extractData.getMaxWaitTime(), extractData.getPatients(), extractData.getLocations(),
                           extractData.getVehicles())
    vehicles = problem_instance.getVehicles()
    activities = problem_instance.getActivities()
    distances_matrix = extractData.getDistanceMatrix()
    ######
    activities.sort(key=lambda x: x.getStartDate())
    monitors_list = []
    # pentru fiecare masina creez un obiect monitor
    for m in vehicles:
        monitors_list.append(Monitor(m))
    printActivities(activities)
    k = 0
    for activity in activities:
        if k < len(vehicles):
            if activity.getType() == 1:
                places_requested_in_car = activity.getPatient().getLoad()
                loadPacientInCar(monitors_list[k], activity, distances_matrix, places_requested_in_car)
                Monitor.choosed_pacients.append(activity.getPatient())
                k += 1
    activities.pop(0)
    activities.pop(0)
    print("---")
    i = 0
    while (len(activities) != 0):
        activity = activities[0]
        while activity.getType() != 0:  # cat timp nu intalnesc o activitate backward
            print("Current :Forward Activity", activity.getID())
            car_monitor = findAvailableCar(monitors_list, activity, distances_matrix)
            if car_monitor != None:
                print(f"Load patient {activity.getPatient().getId()} in car {car_monitor.getCar().getId()}")
                places = activity.getPatient().getLoad()
                loadPacientInCar(car_monitor, activity, distances_matrix, places)
                activities.remove(activity)
                if len(activities) != 0:
                    activity = activities[0]
            else:  # daca masinile sunt full-nu mai pot lua alti pacienti
                print("Unload cars:")
                unloadCars(monitors_list, distances_matrix)
                # de facut reverify conditii daca pot lua pacientul din activitatea curenta
        activity = activities[0]
        while activity.getType() == 0:
            print("Current: Backward activity", activity.getID())
            if checkIfValidActivity(activity,monitors_list[0]) == 0:  # activitatea nu e in succesful_closed_forward_activities
                print(f"Need to deliver forward activity eith id {activity.getID()} first")
                findCarThatHasForwardActivity(monitors_list, activity.getID(),
                                              distances_matrix)  # and remove it from car list
            else:  # daca activitarea e in closed_forward pot sa iau activitatea
                # !!!!!!!!!!!!!!!!!!!!!de facut un check atunci cand car.current_time-activity.startTime<"00h10m"
                car_monitor = findAvailableCar(monitors_list, activity, distances_matrix)
                if car_monitor!=None:
                    print(f"Load patient backward {activity.getPatient().getId()} in car {car_monitor.getCar().getId()}")
                    places = activity.getPatient().getLoad()
                    loadPacientInCar(car_monitor, activity, distances_matrix, places)
                    print("Activities list is ",activities)
                    if len(activities)!=0:
                        activities.remove(activity)
                        if len(activities)!=0:
                            activity = activities[0]
                else:
                    unloadCars(monitors_list,distances_matrix)

    #final checking
    list_fr=monitors_list[0].succesfull_close_activities_forward
    list_bk=monitors_list[0].succesfull_close_activities_backward
    satisfied_requests=getTotalofActivitiesDone(list_fr,list_bk)
    print(satisfied_requests)


main()
