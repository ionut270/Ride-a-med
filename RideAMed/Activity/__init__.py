from enum import Enum


class Activity:
    def __init__(self,id, start_date, end_date,tghome, patient, srvDuration, type_activity):
        self.id=id
        self.start_date = start_date
        self.end_date = end_date
        self.time_to_go_home=tghome
        self.execution_status = False
        self.patient = patient
        self.vehicle = None
        self.srvDuration = srvDuration
        self.type = type_activity

    def getSrvDuration(self):
        return self.srvDuration

    def getStartDate(self):
        return self.start_date

    def getEndDate(self):
        return self.end_date

    def getDuration(self):
        return self.duration

    def getExecutionStatus(self):
        return self.execution_status

    def getPatient(self):
        return self.patient

    def getVehicle(self):
        return self.vehicle

    def setExecutionStatus(self, status):
        self.execution_status = status

    def setVehicle(self, vehicle):
        self.vehicle = vehicle

    def setType(self, typeActivity):
        self.type = typeActivity
    def getID(self):
        return self.id
    def getType(self):
        if self.type==TypeActivity.FORWARD:
            return 1
        else:
            return 0
    def getTimeToGoHome(self):
        return self.time_to_go_home
    # def __gt__(self, other):
    #     if self.end_date > other.getEndDate():
    #         return True
    #     else:
    #         return False

    # def __lt__(self, other):
    #     if self.start_date < other.getStartDate():
    #         return True
    #     else:
    #         return False

    def __str__(self):
        return f"{str(self.patient)} {self.start_date}, {self.end_date}, {self.time_to_go_home}, {self.execution_status}"
    def __repr__(self):
        return str(self)
class TypeActivity(Enum):
    FORWARD = 1
    BACKWARD = 0
