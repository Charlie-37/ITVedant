
# //*---------Swapping------*//

# //*-----Using 2 var

##x = 10
##y = 20

##x = x+y
##y = x - y
##x = x - y
##
##print("x = ", x)
##
##print("y = ", y)

# //*---- Using 3 var

##temp = x
##x = y
##y = temp
##
##print("x = ", x)
##
##print("y = ", y)


# //*-----Febonaccii Series------*//

##i = 0
##x = 0
##y = 1
##while i<10:
##    print(x)
##    z = x+y
##    x = y
##    y = z
##    i+=1
    
# /*--------Finding List value in a list----*//

x = [3,5,1,2,9,5,6,10]
i = 0
mn = 9999999

while i<len(x):
    if x[i]< mn:
        mn = x[i]
        
    i+=1
print(mn)

# /*--------Finding Max value in a list----*//

x = [3,5,1,2,9,5,6,10]
i = 0
mn = -9999999

while i<len(x):
    if x[i]> mn:
        mn = x[i]
        
    i+=1
print(mn)
        
