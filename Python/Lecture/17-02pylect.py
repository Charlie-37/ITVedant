
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

# x = {"a":55,"b":65,"c":56}

# for k,j in x.items():
#     print(k,j)




# //*-----For each---*//
##x = [1,54,6,45,5]
##
##for i in x:
##    print(i)


# l1 = [1,2,3,4,5]
# l2 = [4,5,6,7,8]



# for i in l1[:]:
#     if i in l2:
#         l1.remove(i)
#         l2.remove(i)


# print(l1)
# print(l2)


'''1.Write a Python program find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five.
NOTE:Do not use in-built count function'''

# l1 = [19,19,5,6,5,3,8]
# ninet = 0
# fiv = 0
# for i in l1:
#     if i == 19:
#         ninet+=1

#     if i == 5:
#         fiv += 1

# if ninet == 2 and fiv >=3:
#     print("True")
# else:
#     print("false")




'''2.Write a program to count integers,string,symbols from below given string and store them in different dictionaries.
NOTE:Upper case and lower case alphabets will be stored in different dictionaries
String : '1.SeQueL String is A g00d cOmp@NY'

Dummy Output: int :{1:'2',90:'10'}
upper case :{'A':'4','Y':'1','Z':'3'}      
lower case : {'g':'9','e':'5','j':'23'}
special case : {'@':'2','&':'10'}'''






# from re import X
from numpy import integer


str = '1.SeQueL String is A g00d cOmp@NY'
strList = []
intnum = ["0","1","2","3","4","5","6","7","8","9"]
for i in str:
    strList.append(i)







list1 = [['ca',['cat','cow','lion']],['dad',['dad','danger','cat']]]
list2 = []
for i in list1:

    if i[0] in i[1]:
            print(i[1])
            list[i[1]]

    for j in i:
        # print(j)
        # if i[0] in i[1]:
        #     print(i[1])
        #     list[i[1]]

        if j[0] in j[1]:
            print(j[0])
            print(j[1])
            list[j[1]]
        







    
    


