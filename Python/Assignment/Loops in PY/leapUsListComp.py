
leapY = [i for i in range(1900,2030) if (i%400==0) or (i%100!=0)and(i%4==0)]
print(leapY)