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
            forwardActivity = Activity(extractDurationFromStringInSeconds(patient.getRdvTime()) - self.maxWaitTime,
                                       extractDurationFromStringInSeconds(patient.getRdvTime()),
                                       patient,
                                       extractDurationFromStringInSeconds(patient.getSrvDuration()),
                                       TypeActivity.FORWARD)
            backwardActivity = Activity(extractDurationFromStringInSeconds(patient.getRdvTime()) + extractDurationFromStringInSeconds(patient.getRdvDuration()),
                                        extractDurationFromStringInSeconds(patient.getRdvTime()) + self.maxWaitTime + extractDurationFromStringInSeconds(patient.getRdvDuration()),
                                        patient,
                                        extractDurationFromStringInSeconds(patient.getSrvDuration()),
                                        TypeActivity.BACKWARD)
            self.activities.append(forwardActivity)
            self.activities.append(backwardActivity)

    def getActivities(self):
        return self.activities

    def getPatients(self):
        return self.patients

    def getVehicles(self):
        return self.vehicles
