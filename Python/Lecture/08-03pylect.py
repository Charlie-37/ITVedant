##Lambda Function
##
##
##Arthematic Operations
##
##Addition
##add = lambda x,y:x+y
##print("Addition is :", add(2,3))
##
##
##Subtraction
##sub = lambda x,y:x-y
##print("Substraction is : ", sub(12,3))
##
##
##Multiplication
##mult = lambda x,y:x*y
##print("Multiplication is : ", mult(6,8))
##
##
##Division
##divs = lambda x,y:x/y
##print("Division is : ", divs(50,10))
##
##
##Floor Division
##floord = lambda x,y:x//y
##print("Floor Division is :", floord(80,8))
##
##
##Power
##powr = lambda x,y:x**y
##print("Power is :", powr(2,8))
##
##Modulus
##mds = lambda x,y:x%y
##print("Modulus is :", mds(2,8))
##


# //*-------------Mapping/Filter------------*//


##def pald(n):
##    n1 = n
##    res = 0
##    while n!=0:
##        rem = n%10
##        res = (res*10)+rem
##        n//=10
##
##    if res == n1:
##        return res
##    else:
##        return ''
##
##
##lst1=[1,153,101,914,453,414]
##
##plaL = list(filter(pald,lst1))
##
##print(plaL)



# //*-----------Sorting-------*//

##names = ["Sunil g Bhave" ,"Sagar gare", "Bhavesh Ainkar", "Sneha bhalerao","Tejas B Jadhav"]
##
##names.sort(key= lambda name: name.lower().split()[-1])
##print(names)




# //*---------Celc to Fhernhite---*//

cities = [("Mumbai",25),("Delhi",56),("Banglore",24),("Shimla",2)]

celtof = lambda d:(d[0],(9/5 * d[1] +32))

fah = list(map(celtof,cities))
print(fah)














