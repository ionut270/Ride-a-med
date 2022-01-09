def addTime(first_time:str, second_time:str)->str:
        h_m1=getHoursMinutes(first_time)
        h_m2=getHoursMinutes(second_time)
        hours=0
        if h_m1[1]+h_m2[1]>60:
            hours+=1
            minutes=h_m1[1]+h_m2[1]-60
        hours=h_m1[0]+h_m2[0]+hours
        if hours>=24:
            return f"1d{hours-24}h{minutes}m"
        else:
            return f"{hours}h{minutes}m"
def getHoursMinutes(time:str):
    hours=time.split("h")
    minutes=hours[1].split("m")
    return int(hours[0]),int(minutes[0])
def compareTime(time1,time2):
    h_m1 = getHoursMinutes(time1)
    h_m2 = getHoursMinutes(time2)
    if h_m1[0]<h_m1[0]:
        return 1
    elif h_m1[1]<h_m2[1] and h_m1[0]==h_m2[0]:
        return 1
    else:
        return 0

print(getHoursMinutes("07h34m"))
print (addTime(first_time="07h34m",second_time="16h50m"))
print(compareTime("08h31m","07h33m"))