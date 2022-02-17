

# //*--------Swaping--------*/

##
##y = x-y
##x = x-y
##
##print("x = ", x)
##print("Y = ", y)
##


# //*-----BY temp value----*//

##x = 20
##y = 10
##
##temp = x
##x = y
##y = temp
##
##print("X = ", x)
##print("Y = ", y)
##



# //*----------Febonacii series--------*//

##x = 0
##y = 1
##i = 0
##
##while i<10:
##    print(x)
##    z = x+y
##    x = y
##    y =z
##    i+=1
##    

# //*-----Finding least value in the list-----*//

##x = [2,34,53,5,1,-9,5,2]
##inf = 9999999
##i = 0
##
##while i<len(x):
##    if x[i]<inf:
##        inf = x[i]
##    i+=1
##print(inf)


# //*-------Finding greates value in the list-------*//


##x = [23,22,35,63,1,32,76,4]
##inc = -9999999
##i = 0
##
##while i<len(x):
##    if x[i]>inc:
##        inc = x[i]
##    i+=1
##print(inc)



# //*------Sorting list-----*//
##x = [22,43,52,87,42,9,0,12,1]
##
##for i in range(len(x)+1):
##    for j in range(i+1, len(x)):
##        if x[i]>x[j]:
##            temp = x[i]
##            x[i] = x[j]
##            x[j] = temp
##print(x)


# /*---;------**----//

##for i in range(1,4):
##    print(i)
##    print(i)
##    print(i)
##print(i)


# //*-------Dictonary--*/
##d = {
##    "a" : [10,20,30],
##    "b" : [5,4,3]
##    }

#print(d)
##for i,j in d.items():
##    res = 0
##    for k in range(0, len(j)):
##        res = res+j[k]
##    print(i,res)
    
# /*------Tupple add---------*//
x = [(45,2),(655,52,23),(45,32)]
y=[]

for i in x:
    j=list(i)
    res=0
    for k in j:
        res=res+k
    y.append(res)

print(y)


##x = [7,3,4,2]
##
##for i in range(len(x)):
##    for j in range(i+1, len(x)):
##        if x[i]>x[j]:
##            #x[i],x[j] = x[j],x[i]
##            temp = x[i]
##            x[i] = x[j]
##            x[j] = temp
##print(x)














































