

# Lambda Function

##x = lambda z,y: z+y
##
##sum=x(10,12)
##print(sum)


# Mapping/Filter

##list1 = [12,323,425,31213,485,969]
##
##
##def pald(n):
##    n1 = n
##    res = 0
##    while n!=0:
##        rem = n%10
##        res = (res*10)+rem
##        n//=10
##        
##    if n1 == res:
##        return res
##    else:
##        return ''
##
##list2=list(filter(pald,list1))
##print(list2)


# Filter using sort n lambda

##names = ["sunil g Bhave", "Sneha b bhalerao", "ainkar Bhavesh", "Tejas jadhav"]
##
##names.sort(key=lambda name:name.lower().split()[-1])
##print(names)

n = 47

for i in range(2,n):
    if n%i==0:
        print("not prime")
        break

else:
    print("Prime")

























