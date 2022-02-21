
# /*----Even ODD binary conv---*//
##x = 15283529
##
##b = ""
##
##for i in str(x):
##    if int(i)%2 ==0:
##        b = b + "0"
##    else :
##        b = b+"1"
##
##print(b)


# //*----Palindrome-------*//
##x = int(input("Enter the Number to check Palindrom : "))
##y = x
##str1  = str(x)
##res=0
##
##for i in range(len(str1)):
##    rem = x%10
##    res = (res*10)+rem
##    x = x//10
##
##print(res)
##
##if y == res:
##    print("Palindrom")
##else:
##    print("Not palindrom")
##    


# //-----Armstrong Number-----*//

x1 = 153
x2 = x1
x3 = x1
d = 0
tot = 0

while (x1!=0):
    x1 = x1//10
    d = d+1

#print(d)

while (x2!=0):
    rem = x2%10
    tot = tot + (rem**d)
    x2 = x2//10
print(tot)


if tot == x3:
    print(f"{x3} is Armstrong number")

else :
    print(f"{x3} is Not Armstrong number")

































    
    
