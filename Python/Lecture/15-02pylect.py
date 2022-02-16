
# //*----------Even Odd---------*//
##x = int(input("Enter the number : " ))
##
##if x %2 == 0:
##    print("Number is Even")
##else :
##    print("Number is ODD")
              
# //*-------Laep Year------------------*//

##x= int(input("Enter the Year : "))
##
##if x%4==0:
##    if x%100==0:
##        if x%400==0:
##            print("Leap Year")
##        else:
##            print("Not a Leap year")
##    else:
##        print("Leap Year")
##else:
##    print("Not a Leap Year")
##

# //*----------Calculator------------------*//

##x = float(input("Enter the First Number : "))
##y = float(input("Enter the second Number : "))
##opert = input("Enter the Operator : ")
##
##if opert=="+":
##    print(x, opert, y,"=",  x+y)
##    
##elif opert == "-":
##    print(x, opert, y,"=",  x-y)
##
##elif opert == "/":
##    print(x, opert, y,"=",  x/y)
##
##elif opert == "*":
##    print(x, opert, y,"=",  x*y)
##
##elif opert == "**":
##    print(x, opert, y,"=",  x**y)
##
##elif opert == "%":
##    print(x, opert, y,"=",  x%y)
##
##elif opert == "//":
##    print(x, opert, y,"=",  x//y)
##
##else :
##    print("Invalid Operator")
##    
##

# //*----------Grade------------------*//

##x = int(input("Enter the Percentage : "))
##
##if x>=75 and x<100:
##    print("Grade is A ")
##
##elif x>=60 and x<75:
##    print("Grade is B ")
##
##elif x>35 and x<60:
##    print("Grade is C ")
##
##elif x<35 :
##    print("Fail ")
##
##else:
##    print("Invalid Percentage ")



# //*----------Factorial------------------*//

##x  = int(input("Enter the number to find factorial : "))
##
##res = 1
##fact = 1
##
##while fact<=x:
##    res = res * fact
##    fact +=1
##print(res)

# //*----------num add------------------*//

##x  = int(input("Enter the number to find the sum : "))
##
##res = 0
##sumt = 1
##
##while sumt<=x:
##    res = res + sumt
##    sumt +=1
##print(res)


# //*----------table------------------*//

##x  = int(input("Enter the number for table : "))
##
##res = 1
##tabt = 1
##
##while tabt<=10:
##    res = tabt * x
##    
##    print(x, "*", tabt, "=", res)
##    tabt +=1

   
# //*----------Console base calsi------------------*//

##while(True):
##    print("Welcome to my calculator \n")
##    
##    print("Enter 1 for Addition : ")
##    print("Enter 2 for Substraction : ")
##    print("Enter 3 for Multiplication : ")
##    print("Enter 4 for Division : ")
##    print("Enter 5 for Modulo : ")
##    print("Enter 6 for Power : ")
##    print("Enter 7 for Floor Devision : ")
##    print("Enter 8 for Exit : ")
##
##    
##    opert = input("Enter the Your Choice : ")
##   
##
##    if opert=="1":
##         x = float(input("Enter the First Number : "))
##         y = float(input("Enter the second Number : "))
##         print(x,"+", y,"=",  x+y)
##        
##    elif opert == "2":
##         x = float(input("Enter the First Number : "))
##         y = float(input("Enter the second Number : "))
##         print(x,"-", y,"=",  x-y)
##    
##    elif opert == "3":
##        x = float(input("Enter the First Number : "))
##        y = float(input("Enter the second Number : "))
##        print(x,"*", y,"=",  x*y)
##    
##    elif opert == "4":
##        x = float(input("Enter the First Number : "))
##        y = float(input("Enter the second Number : "))
##        print(x,"/", y,"=",  x/y)
##    
##    elif opert == "5":
##        x = float(input("Enter the First Number : "))
##        y = float(input("Enter the second Number : "))
##        print(x,"%", y,"=",  x%y)
##    
##    elif opert == "6":
##        x = float(input("Enter the First Number : "))
##        y = float(input("Enter the second Number : "))
##        print(x,"**", y,"=",  x**y)
##    
##    elif opert == "7":
##        x = float(input("Enter the First Number : "))
##        y = float(input("Enter the second Number : "))
##        print(x,"//", y,"=",  x//y)
##    
##    elif opert == "8":
##        exi = input("Do You want to Exit type Y/N : ")
##        exi = exi.lower()
##        if exi == "y":
##            break
##        elif exi == "n":
##            continue
##        else:
##            print("Invalid Input")
##


x = [2,9,7,4,3,5,10]
i = 0
res = 0
##while i<len(x):
##    
##    if x[i]%2 ==0:
##        res = res + x[i]
##    i+=1
##print(res)

# //*------Using Range----*//
##for j in range(0, len(x)):
##    if x[j]%2 ==0 :
##        res = res + x[j]
##print(res)



inc = 0
envl = []
odl =[]
while inc<len(x):
    if x[inc]%2 == 0:
        envl.append(x[inc])
        
    elif x[inc]%2 != 0:
        
        odl.append(x[inc])
    inc+=1
print("Even list", envl)
print("Odd list", odl)
    
    
    
















