
# //*-----Range--------*//

##x = [45,461,4,1,62,9,1]
##
##y = list(range(0,12))
##print(y)
##
##z = list(range(12,0,-1))
##print(z)


# //*-----Foor loop--------*//

##for i in range(1,6):
##    print(i)



# /*-----NOT in------*//
##x = ["Green", "Red"]
##y = "Green" not in x
##print(y)
##
##a = "Python"
##b = "PythoN"
##print(a>b)
##

#//*----------------------- FOR LOOP Program----------------------*//

# /*-----Table using For loop---*//

##x = 5
##res = 0
##for i in range(1,11):
##    res = i * x
##    print(x, "*", i, "=",res)


# /*-----Table using For loop reverse---*//

##x = 5
##res = 0
##for i in range(10,0,-1):
##    res = i * x
##    print(res)
    


# //*-------Factorial using for---*//

##x = 5
##res = 1
##
##for i in range(1, x+1):
##    res = res * i
##print(res)


# //*--------Febonacii---------*//

##t = 10
##x = 0
##y = 1
##
##for i in range(0, t):
##    print(x, end = " ")
##    z = x+y
##    x = y
##    y = z

# //*------Num Reverse-----*//

# //*---- Using FOR loop
##x = 1234
##y = str(x)    # Convert it into string to get length
##rev = 0
##
##for i in range(len(y)):
##    
##    rem = x%10
##    rev = (rev *10)+rem
##    x = x//10
##
##print(rev)

# //*-------Using While loop----*//

##x = 1234
##rev = 0
##
##while x!=0:
##    rem = x%10
##    rev = (rev *10) +rem
##    x = x//10
##print(rev)

# //*--------Palindrome----*//

##x = 123454321
##x1 = x
##rev = 0
##while x!=0:
##    rem = x%10
##    rev = (rev * 10)+rem
##    x //= 10
##print(rev)
##
##if x1==rev:
##    print("Palindrome")
##else:
##    print("Not Palindrome")


# //*------- Finding Min------*//

##x = [12,56,5,2,7,8,5]
##maxn = 9999999
##
##for i in range(len(x)):
##    if x[i] < maxn:
##        maxn = x[i]
##print(maxn)

# //*------Dictionary items----*//

x = {"a":55,"b":65,"c":56}

for k,j in x.items():
    print(k,j)




# //*-----For each---*//
##x = [1,54,6,45,5]
##
##for i in x:
##    print(i)

















