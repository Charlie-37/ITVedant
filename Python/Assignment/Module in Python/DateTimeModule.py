import datetime as dt

help = dir(dt)
print(help)

# //*------------Date---------*//


exDate = dt.datetime(1999, 4, 2)


# //*-------Year-----------*//
yearDate = exDate.year
print(yearDate)

# //*---  Month---------*//

monthDate = exDate.month
print(monthDate)

# //*---  Date-------*//

DtDate = exDate.day
print(DtDate)

# //*--------Time Delta---------*//

timeDt = dt.timedelta(hours = 11, minutes=45, seconds = 15)
print(timeDt)

# //*--------strftime---------*//
nowTime = dt.datetime.now()
print(nowTime)

nowHrs = nowTime.strftime("%H")
print(nowHrs)

nowmin = nowTime.strftime("%m")
print(nowmin)

nowsec = nowTime.strftime("%S")
print(nowsec)

nowyear = nowTime.strftime("%Y")
print(nowyear)

nowmonth = nowTime.strftime("%m")
print(nowmonth)

noweek = nowTime.strftime("%w")
print(noweek)


# //*-------strptime---------*//

dateobj = dt.datetime.strptime("09/23/2030 8:28","%m/%d/%Y %H:%M")
print(dateobj)



# //*---------TIME-----------*//

NowTime = dt.datetime.now().time()

nowHour = NowTime.hour
print(nowHour)

nowMin = NowTime.minute
print(nowMin)

nowSec = NowTime.second
print(nowSec)