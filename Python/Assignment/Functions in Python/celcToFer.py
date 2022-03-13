

''' using map function,  create a lambda expression to convert the degree celcius to fahrenheit
temp = [('kashmir',1),('mumbai',16),('goa',22),('channai',18),('kerla',20)]
Formula to convert fahrenheit to celsius, f = 9/5 x c + 32
'''
temp = [('kashmir',1),('mumbai',16),('goa',22),('channai',18),('kerla',20)]

celToFer = lambda a:(a[0],((9/5) * a[1] + 32))
    

list2 = list(map(celToFer,temp))
print(list2)