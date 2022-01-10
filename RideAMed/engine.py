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
    succesfull_close_activities=[]
    choosed_pacients=[]
    def __init__(self,car:Vehicle):
        self.car=car
        self.car_depo=car.getStart_depot()
        self.car_capacity=car.getCapacity()
        self.list_activities_forward=[]
        self.list_activities_backward=[]
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
            self.car_capacity+=places
        else:
            self.car_capacity-=places
    def restoreCarCapacity(self):
        self.car_capacity=self.car.getCapacity()
    def getCurrentTime(self):
        return self.current_time
    def setNewPostion(self,poz):
        self.current_position=poz
    def getCurrentPosition(self):
        return self.current_position
    def getCar(self):
        return  self.car
    def getForwardActivities(self):
        return self.list_activities_forward
    def addActivityForward(self,activity):
        self.list_activities_forward.append(activity)
    def updateCurrentTime(self,new_time):
        new_current_time=addTime(self.current_time,self.convertFromMinutesToHM(new_time))
        self.current_time=new_current_time
    def __str__(self):
        return  f"{self.car.getId()},{self.list_activities_forward}"
    def convertFromMinutesToHM(self,minutes):
        h,m=divmod(minutes,60)
        return f"{h}h{m}m"
    def getRemainingTime(self):
        tm=[]
        for ac in self.list_activities_forward:
            tm.append(subtractTime(self.current_time,ac.getPatient().getRdvTime()))
        return tm
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
    if car_monitor.car_capacity-activity.getPatient().getLoad()<0:
        return 0
    return 1

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
    fr_activities=sorters.getForwardActivities(activities)
    fr_activities.sort(key=lambda x:x.getStartDate())

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
            monitors_list[k].addActivityForward(activity)
            #timpul curent al masinii
            monitors_list[k].updateCurrentTime(distances_matrix[monitors_list[k].car_depo][activity.getPatient().getStartLocation()])
            #poztia masini-><devine pozitia primului pacient
            monitors_list[k].setNewPostion(activity.getPatient().getStartLocation())
            #capacitatea masinii=capacitatea_masinii-nr_de_locuri_dorite_de_un-pacient
            monitors_list[k].updateCarCapacity(activity.getPatient().getLoad())
            Monitor.choosed_pacients.append(activity.getPatient())
            k+=1
    for m in monitors_list:
        print(m.getCurrentPosition(),m.getCurrentTime())
        print("When patient need to get med_center",m.list_activities_forward[0].getPatient().getRdvTime())
        print("Remaining timne")
        print(m.getRemainingTime(),m.getCurrentCarCapacity())
    #logica principala dupa ce ne-am asigurat ca fiecare masina are un prim_pacinet
    ####CREATE GRAPH
    # g=createGraph(distances_matrix,locations)
    # result=g.dijkstra(8)
    #print(result)
    #print(getMinimumFromDictonar(result,4,20))
    for a in fr_activities:
        print(convertFromSecondsToHM(a.getStartDate()),a.getPatient().getStartLocation(),a.getPatient().getDestination())
    activity3=fr_activities[2]
    flag,car_monitor=assignNextActivityToACar(monitors_list,activity3,distances_matrix)
    if flag==1:
        load_flag=checkCarLoad(car_monitor,activity3)
        if load_flag==1:#pot lua pacientul in masina
            car_monitor.addActivityForward(activity3)
    #####NEXT de implementat si pentru celealte
        #de facut logica cand masina nu mai poate lua pacienti
    #
getSolution()
