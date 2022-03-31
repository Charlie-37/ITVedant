# //*------- MAP-----*//
list1= [21,9,3,7,6,35]

def nsq(n):
    return n**2
sqlist1 = list(map(nsq,list1))

print("Square of the list elements :",sqlist1)


# //*------- Filter-----*//

list2 = [1,52,66,32,21,36]

def evennum(n):
    if n%2==0:
        return n
    else:
        pass

evenlist2 = list(filter(evennum,list2))
print("Even elements from the list are :",evenlist2)

# //*------- reduce-----*//

from functools import reduce

list3 = [11,65,95,23,36,45]
sumlist3 = reduce(lambda x,y: x+y, list3)
print("Sum of all List Elements : ",sumlist3)


# //*---List Comprenhesion-----*//

list4 = [x for x in range(100)if(x%5==0)]
print(list4)


# //*--- Lambda-----*//

list5 = [1,9,6,7,5,4]
cubeele = list(map(lambda x: x**3, list5))
print("Cube of the elements is : ",cubeele)


##cities = [("Mumbai",10),("Delhi",23),("Jaipur",25)]
##
##def tepcov(k):
####    for i,j in cities:
####        j = j*(9/5)+32
####        return(i,j)
##
##    
####    d[1]=(9/5 * d[1] +32)
####    return(d[0],d[1])
##
##    for i,j in k:
##        return(i,j)
##
####cip = list(map(tepcov,cities))
####print("Cities Celcius to Ferhannites :",cip)
##
##
##
##
###pg = tepcov(cities)
##pg = list(map(tepcov,cities))
##print(pg)






d = [{"apple",10},{"mango",8},{"grapes",9}]































