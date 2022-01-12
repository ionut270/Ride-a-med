from ExtractData import ExtractData
from PTP import PTP
from Vehicle import Vehicle
import sorters
from graph import Graph,Node,Edge
from timeCalculator import addTime,subtractTime,convertFromSecondsToHM,compareTime
from Activity import Activity
class PacientTimeMonitor:
    def __init__(self,patient,time_remain):
        self.patient=patient
        self.time_remain=time_remain
    def updateTimeRemain(self,new_time):
        self.time_remain=new_time
class Monitor:
    succesfull_close_activities_forward=[]
    succesfull_close_activities_backward =[]
    choosed_pacients=[]
    def __init__(self,car:Vehicle):
        self.car=car
        self.car_depo=car.getStart_depot()
        #self.car_capacity=car.getCapacity()
        self.car_capacity =0
        self.list_activities=[]
        self.current_time=car.getStartTime()
        self.current_position=car.getStart_depot()
    def getCurrentCarCapacity(self):
        return self.car_capacity
    def updateCarCapacity(self,places,load=True):
        """cand urca un pacient facem update cu locurile cerute de acesta-respectiv scadem
            cand coboara un pacient adunam locurile lasate libere pentru a mentine numarul de locurile
            pe care il avem la dispozitie
            load-True->in masina urca pacient
            places=pacient.getLaod()
        """
        if load==False:
            self.car_capacity-=places
        else:
            self.car_capacity+=places
    def restoreCarCapacity(self):
        self.car_capacity=self.car.getCapacity()
    def getCurrentTime(self):
        return self.current_time
    def setNewPosition(self,poz):
        self.current_position=poz
    def getCurrentPosition(self):
        return self.current_position
    def getCar(self):
        return  self.car
    def getForwardActivities(self):
        return self.list_activities
    def addActivityForward(self,activity):
        self.list_activities.append(activity)
    def updateCurrentTime(self,new_time):
        new_current_time=addTime(self.current_time,self.convertFromMinutesToHM(new_time))
        self.current_time=new_current_time
    def __str__(self):
        return  f"{self.car.getId()},{self.list_activities}"
    def convertFromMinutesToHM(self,minutes):
        h,m=divmod(minutes,60)
        return f"{h}h{m}m"
    def getRemainingTime(self):
        tm=[]
        for ac in self.list_activities:
            if ac.getType()==1:
                sub=subtractTime(self.current_time,ac.getPatient().getRdvTime())
                tm.append(subtractTime(sub,ac.getPatient().getSrvDuration()))
            else:
                sub=subtractTime(self.current_time,convertFromSecondsToHM(ac.getEndDate()))
                tm.append(subtractTime(sub,ac.getPatient().getSrvDuration()))
        return tm
    def removeActivity(self,activity):
        self.list_activities.remove(activity)
def createGraph(matrix,locations):
    nodes_list = []
    edges_list = []
    for location in locations:
        nodes_list.append(Node(location))
    for i in range(0, len(matrix)):
        for j in range(i + 1, len(matrix[0])):
            edges_list.append(Edge(i, j, matrix[i][j]))
    g = Graph(nodes_list, edges_list)
    return g
def getMinimumFromDictonar(dictio:dict,car_depo:int,current_postion:int):
    minimum=10_000
    result_key=-1
    for key in dictio.keys():
        if dictio[key]<minimum and key!=car_depo and key!=current_postion:
            minimum=dictio[key]
            result_key=key
    print(result_key,minimum)
    return  result_key,minimum

def getPossibleCar(monitors:list,activity:Activity,matrix):
    minim = 10000
    save_monitor=None
    for m in monitors:
        new_patient_position = activity.getPatient().getStartLocation()
        distance = matrix[m.getCurrentPosition()][new_patient_position]
        if distance < minim:
                minim = distance
                save_monitor = m
    return save_monitor
def getAvailableCar(monitors,activity):
    for m in monitors:
        if checkCarLoad(m,activity)!=-1:
            return m
def assignNextActivityToACar(monitors:list,activity:Activity,matrix):
    """verific daca pot asigna activitatea unei masini
    Activiatea are un pacient asignat-de vazut constructia clasei activity
    """
    #iau ultimul pacient din fiecare lista
    ##si vad de la  care ar fi distanta minima pana la p3->iau monitorul aferent
    mon = getPossibleCar(monitors, activity, matrix)
    ###sa calculez o lista de distante
            #pentru fiecare pacient din lista deja existenta calculez
    ##### remaintime-distanta(p_current,p3)-distanta(p3,destinatia_lui_pi)
    ####Si daca cumva remain_time<=0 nu-l iau daca remain_time>0 atunci osa pot sa il asignez
    remain_time_list=mon.getRemainingTime()
    calculated_distances=[]
    next_patient_poz=activity.getPatient().getStartLocation()
    current_position=mon.getCurrentPosition()
    for i in range(0,len(remain_time_list)):
        #daca lista masinii are mai multi pacienti
        pacienti=mon.getForwardActivities()[i].getPatient()
        destination_of_pacienti=pacienti.getDestination()#destinatia pacientului i
        sum=subtractTime(remain_time_list[i],convertFromSecondsToHM(matrix[current_position][next_patient_poz]))# remain_time al pacientului 1- distanta in timp de la pozitia curenta a masinii pana la pozitia noului pacient
        final_distance=subtractTime(sum,convertFromSecondsToHM(matrix[current_position][destination_of_pacienti]))# din sum scad distanta in timp de la noul pacient la destiantia pacientuluii
        calculated_distances.append(final_distance)
    flag=verifyRemaningTime(calculated_distances)
    return flag,mon
def verifyRemaningTime(calculated_time_distances:list):
    for rt in calculated_time_distances:
        if compareTime(rt,"00h00m")<0:#compareTime-return -a daca t1<t2 ,0 t1=t2,1 t1>t2 timpul daca ca si string
            return 0
    return 1
def checkCarLoad(car_monitor:Monitor,activity):
    """verific daca pot sa iau pasagerul in masina"""
    car_current_capacity=car_monitor.getCurrentCarCapacity()
    pacient_places_in_car=activity.getPatient().getLoad()
    new_capacity=car_current_capacity+pacient_places_in_car
    if new_capacity>=car_monitor.getCar().getCapacity():
        return -1
    return pacient_places_in_car

def getSolution():
    extractData = ExtractData("E:\\anul III\\AI\\date_proiect\\easy\PTP-RAND-1_4_2_16.json")
    problem_instance = PTP(extractData.getMaxWaitTime(), extractData.getPatients(), extractData.getLocations(),
                       extractData.getVehicles())
    #####
    locations = problem_instance.getLocations()
    patients = problem_instance.getPatients()
    med_centers = sorters.getMedCEnters(locations)
    vehicles=problem_instance.getVehicles()
    depos = sorters.getDepos(locations)
    depos_indexes = [dep.getId() for dep in depos]
    activities=problem_instance.getActivities()
    distances_matrix=extractData.getDistanceMatrix()
    ######
    activities.sort(key=lambda x: x.getStartDate())
    # fr_activities=sorters.getForwardActivities(activities)
    # fr_activities.sort(key=lambda x:x.getStartDate())
    fr_activities=activities
    monitors_list=[]
    #pentru fiecare masina creez un obiect monitor
    for m in vehicles:
        monitors_list.append(Monitor(m))
    k=0

    #pentru fiecare masina ii asignez primii 2 pacienti in ordinea timpului in care trebuie ridicati
    #asignandu-le fiecaruia cate o masina
    ##o activitate are un pacient deci activitate este acelasi timp pacient numai ca are alte timpuri calculate
    for activity in fr_activities:
        if k<len(vehicles):
            print("loaod: ",activity.getPatient().getLoad())
            if activity.getType()==1:
                monitors_list[k].addActivityForward(activity)
                #timpul curent al masinii
                monitors_list[k].updateCurrentTime(distances_matrix[monitors_list[k].car_depo][activity.getPatient().getStartLocation()])
                #poztia masini-><devine pozitia primului pacient
                monitors_list[k].setNewPosition(activity.getPatient().getStartLocation())
                #capacitatea masinii=capacitatea_masinii-nr_de_locuri_dorite_de_un-pacient
                monitors_list[k].updateCarCapacity(activity.getPatient().getLoad())
                Monitor.choosed_pacients.append(activity.getPatient())
                k+=1
    for m in monitors_list:
        print(m.getCurrentPosition(),m.getCurrentTime())
        print("When patient need to get med_center",m.list_activities[0].getPatient().getRdvTime())
        print("Remaining timne")
        print(m.getRemainingTime(),m.getCurrentCarCapacity())

    for a in fr_activities:
        print(convertFromSecondsToHM(a.getStartDate()),a.getPatient().getStartLocation(),a.getPatient().getDestination())
    fr_activities.remove(fr_activities[0])
    fr_activities.remove(fr_activities[0])
    print(len(fr_activities))
    while len(fr_activities)>0: #and checkifCarPassedTime(monitors_list)==1:
        i=0
        while i<len(fr_activities):
            activity=fr_activities[i]
            flag,car_monitor=assignNextActivityToACar(monitors_list,activity,distances_matrix)
            print(flag,car_monitor.getCar().getId())
            if flag==1:#exista o posibila asignare a pacientului unei masini
                load_flag=checkCarLoad(car_monitor,activity)
                if load_flag!=-1:#pot lua pacientul in masina
                    print("carr add pacient")
                    flag_valid=checkIfValidActivity(activity,car_monitor)
                    if flag_valid==0:#Daca activitatea forwrd nu a aparut in done_forward_activities
                        carDeliver(car_monitor,car_monitor.get)
                    else:
                        loadPatientToCar(car_monitor,activity,distances_matrix,load_flag)
                        fr_activities.remove(activity)
                        #i=0
                else:
                    print("Car is full")
                    carDeliver(car_monitor,distances_matrix,True)
            else:
                print(f"flag {flag}")
            i+=1
    #final
    for mon in monitors_list:
        print(mon)
        deliverLastPatients(mon,distances_matrix)
        print(len(mon.getForwardActivities()))
    print("final")
    car_monitor=monitors_list[0]
    for a in car_monitor.succesfull_close_activities_forward:
        print(a.getPatient().getId())

    #####NEXT de implementat si pentru celealte
        #de facut logica cand masina nu mai poate lua pacienti
    #
def checkIfValidActivity(activy:Activity,car_monitor):
    if activy.getType()==0:#activitea e backward trebuie sa verific daca cea forward cu acelasi id s-a realizat cu succes si timpul curent al masinii sa si aprox cu cel de start.
        forward_done_activities=[a.getID() for a in car_monitor.succesfull_close_activities_forward]
        if activy.getID() not in forward_done_activities: #or activity.StartTime()-car.getCurrentTime()<5min
            return  0
        else:
            return 1
    else:
        return 2
def loadPatientToCar(car_monitor:Monitor,activity,matrix,load_flag):
    car_monitor.addActivityForward(activity)
    car_monitor.updateCarCapacity(load_flag)
    new_pozition = activity.getPatient().getStartLocation()
    car_monitor.updateCurrentTime(matrix[car_monitor.getCurrentPosition()][new_pozition])
    car_monitor.setNewPosition(new_pozition)
def deliverLastPatients(mon,matrix):
    aclist=mon.getForwardActivities()
    if len(aclist)!=0:
        while(len(aclist)!=0):
            updateOverallCarMonitorForDeliver(mon, aclist[0], matrix)
            aclist=mon.getForwardActivities()
        print("list contain patient")
        # for a in aclist:
        #     updateOverallCarMonitorForDeliver(mon,a,matrix)
def updateOverallCarMonitorForDeliver(car_monitor:Monitor,activity,distances_matrix):
    if activity.getType()==1:
        car_monitor.succesfull_close_activities_forward.append(activity)
    else:
        car_monitor.succesfull_close_activities_backward.append(activity)
    # de facut check cu timpul activitatii
    patient=activity.getPatient()
    car_monitor.updateCarCapacity(patient.getLoad(),False)
    new_pozition = activity.getPatient().getDestination()
    car_monitor.updateCurrentTime(distances_matrix[car_monitor.getCurrentPosition()][new_pozition])
    car_monitor.setNewPosition(new_pozition)
    car_monitor.removeActivity(activity)

def carDeliver(car_monitor:Monitor,matrix, full_flag=False):
    remaining_times=car_monitor.getRemainingTime()
    print(car_monitor.getCurrentCarCapacity())
    aclist=car_monitor.getForwardActivities()
    # while (len(aclist) != 0):
    #     updateOverallCarMonitorForDeliver(car_monitor, aclist[0], matrix)
    #     aclist=car_monitor.getForwardActivities()
    #index=getMinimumIndex(remaining_times)
    print("Remaining times areeee:")
    print(remaining_times)
    for i in range(0,len(aclist)):
        if compareTime(remaining_times[i],"00h20m")==-1:
            updateOverallCarMonitorForDeliver(car_monitor,aclist[i] , matrix)
    if car_monitor.getCurrentCarCapacity()==car_monitor.getCar().getCapacity():
        updateOverallCarMonitorForDeliver(car_monitor,aclist[0] , matrix)
    if full_flag:
        updateOverallCarMonitorForDeliver(car_monitor, aclist[0], matrix)
    print(car_monitor.getCurrentCarCapacity())
    print(car_monitor.getCurrentTime(),"*****************")
def getMinimumIndex(list_of_strings):
    index=0
    minim=list_of_strings[0]
    for i in range(1,len(list_of_strings)):
        if compareTime(list_of_strings[i],minim)==-1:
            index=i
            minim=list_of_strings[i]
    return index
def checkifCarPassedTime(monitor_list):
    for mon in monitor_list:
        if compareTime(mon.getCar().getEndTime(),mon.getCurrentTime())==2:
            return 0
    return 1
def getTotalofActivitiesDone(list_of_forwardActivities,list_of_backward_activities):
    count=0
    for ac in list_of_forwardActivities:
        for bc in list_of_backward_activities:
            if ac.getID()==bc.getID():
                count+=1
    return count
getSolution()
