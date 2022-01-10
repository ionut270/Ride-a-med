def addTime(first_time:str, second_time:str)->str:
        h_m1=getHoursMinutes(first_time)
        h_m2=getHoursMinutes(second_time)
        hours=0
        if h_m1[1]+h_m2[1]>60:
            hours+=1
            minutes=h_m1[1]+h_m2[1]-60
        else:
            minutes=h_m1[1]+h_m2[1]
        hours=h_m1[0]+h_m2[0]+hours
        if hours>=24:
            return f"1d{hours-24}h{minutes}m"
        else:
            return f"{hours}h{minutes}m"
def subtractTime(t1:str,t2:str):
    result=compareTime(t1,t2)
    h_m1 = getHoursMinutes(t1)
    h_m2 = getHoursMinutes(t2)
    if result==-1:
        h_m1 = getHoursMinutes(t2)
        h_m2 = getHoursMinutes(t1)
    elif h_m2[0] == 0:
        h_m1 = getHoursMinutes(t1)
        h_m2 = getHoursMinutes(t2)
    hours = 0

    if h_m1[1] - h_m2[1] < 0:
        hours -= 1
        minutes =h_m1[1]-h_m2[1]+60
    else:
        minutes=h_m1[1]-h_m2[1]
    hours = h_m1[0] - h_m2[0] + hours
    if hours >= 24:
        return f"1d{hours - 24}h{minutes}m"
    else:
        return f"{hours}h{minutes}m"
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
def convertFromSecondsToHM(secondss):
        m,s=divmod(secondss,60)
        h,m=divmod(m,60)
        return f"{h}h{m}m"
# print(getHoursMinutes("07h34m"))
# print (addTime(first_time="11h19m",second_time="2h27mm"))
# print(compareTime("15h35m","05h40m"))
# print (subtractTime("18h15m","10h30m"))
# print (subtractTime("00h15m","01h30m"))
print(compareTime("00h15m","00h00m"))