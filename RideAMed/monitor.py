from Vehicle import Vehicle
from Vehicle import Vehicle
import sorters
from graph import Graph,Node,Edge
from timeCalculator import addTime,subtractTime,convertFromSecondsToHM,compareTime
from Activity import Activity
class Monitor:
    succesfull_close_activities_forward=[]
    succesfull_close_activities_backward =[]
    choosed_pacients=[]
    def __init__(self,car:Vehicle):
        self.car=car
        self.car_depo=car.getStart_depot()
        self.car_capacity=car.getCapacity()
        #self.car_capacity =0
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
            self.car_capacity+=places
        else:
            self.car_capacity-=places
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
    def getCarActivities(self):
        return self.list_activities
    def addActivityToCar(self,activity:Activity):
        self.list_activities.append(activity)
    def updateCurrentTime(self,new_time:str):
        """update currentime cu timp din matricea de distante"""
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