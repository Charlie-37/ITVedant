leap=[]
print("Leap Year from 1900 to 2030 are : ")
for i in range(1900,2030):
    if i % 4 ==0:
        if i %100 == 0:
            if i % 400 == 0:
                leap.append(i)
        else:
            leap.append(i)
print(leap)