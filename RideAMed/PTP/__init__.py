import re
from Activity import Activity, TypeActivity


def getDictionaryTimeFromString(stringTime):
    time_dictionary = {
        'd': 'days',
        'h': 'hours',
        'm': 'minutes',
        's': 'seconds',
    }
    pattern = r'[0-9]+[s|m|h|d]{1}'
    return {time_dictionary[p[-1]]: int(p[:-1]) for p in re.findall(pattern, stringTime)}


def extractDurationFromStringInSeconds(stringTime):
    new_dict = getDictionaryTimeFromString(stringTime)
    return new_dict['hours'] * 3600 + new_dict['minutes'] * 60


class PTP:
    def __init__(self, maxWaitTime, patients, locations, vehicles):
        self.maxWaitTime = extractDurationFromStringInSeconds(maxWaitTime + 'm')
        self.patients = patients
        self.vehicles = vehicles
        self.locations = locations
        self.activities = []
        for patient in self.patients:
            start_date=extractDurationFromStringInSeconds(patient.getRdvTime()) - self.maxWaitTime

            end_date=extractDurationFromStringInSeconds(patient.getRdvTime())+extractDurationFromStringInSeconds(patient.getRdvDuration())

            time_to_go_home=end_date+self.maxWaitTime

            duration=extractDurationFromStringInSeconds(patient.getRdvDuration())

            forwardActivity = Activity(start_date,end_date,time_to_go_home,patient,duration,TypeActivity.FORWARD)
            backwardActivity = Activity(forwardActivity.getEndDate(),forwardActivity.getTimeToGoHome(),time_to_go_home,patient,duration,TypeActivity.BACKWARD)
            self.activities.append(forwardActivity)
            self.activities.append(backwardActivity)

    def transformToHoursMiunutes(self,secondss):
        m, s = divmod(secondss, 60)
        h, m = divmod(m, 60)
        return f"{h}h{m}m"
    def getActivities(self):
        return self.activities

    def getPatients(self):
        return self.patients

    def getVehicles(self):
        return self.vehicles
    def getLocations(self):
        return self.locations