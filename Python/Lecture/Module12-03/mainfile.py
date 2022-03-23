
##import mymaths as mm
##
##print(mm.add(2,4))
##print(mm.sub(12,4))
##print(mm.div(24,4))
##print(mm.mul(2,6))
##print(mm.mod(62,4))
##print(mm.floor(200,4))
##print(mm.powe(2,8))

#//*----------**---------*//

##from mymaths import *
##
##print(add(2,56))
##print(sub(12,4))
##print(div(24,4))
##print(mul(2,6))
##print(mod(62,4))
##print(floor(200,4))
##print(powe(2,8))
##

#//*------------**----------//

##from mymaths import powe
##
##print(powe(2,5))


# //*---------DATE Time----------*//

import datetime as dt

timeNow = dt.datetime.now()
print(timeNow)

dateNow = dt.datetime.now().date()
print(dateNow)

timed = dt.timedelta(30)
print(dateNow + timed)

tdmean = dt.datetime.today()
print(tdmean.strftime("%B %d %Y"))
