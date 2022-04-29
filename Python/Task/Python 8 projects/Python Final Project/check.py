import random as rd
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
# rendom = 0
# for i in range(0,5):
#     rendom = (rendom*10) +rd.randint(0,9)


# print(rendom)
# from datetime import date

# today = date.today()
# print(today)

data=[1,2,54,6,5,8]

def rd():
    import random as rd
    x = rd.randint(0,9)
    return x

# i=0
# x = rd()
# print("created",x)
# while i<= len(data):
    
#     # x = (88,)
#     if x not in data:
#         print("not there",x)
#         data.append(x)
#         break
#     else:
#         print("there", x)
#         x = rd()

# print(data)

# CurDate = datetime.today().strftime("%y-%m-%d")
CurDate = datetime.now()+ relativedelta(years=7)
CurDate1 = datetime.now().strftime("%Y-%m-%d")
print(CurDate)
