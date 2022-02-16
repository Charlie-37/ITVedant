# //*----------Console base calsi------------------*//

while(True):
   print("Welcome to my calculator \n")
   
   print("Enter 1 for Addition : ")
   print("Enter 2 for Substraction : ")
   print("Enter 3 for Multiplication : ")
   print("Enter 4 for Division : ")
   print("Enter 5 for Modulo : ")
   print("Enter 6 for Power : ")
   print("Enter 7 for Floor Devision : ")
   print("Enter 8 for Exit : ")

   
   opert = input("Enter the Your Choice : ")
  

   if opert=="1":
        x = float(input("Enter the First Number : "))
        y = float(input("Enter the second Number : "))
        print(x,"+", y,"=",  x+y)
       
   elif opert == "2":
        x = float(input("Enter the First Number : "))
        y = float(input("Enter the second Number : "))
        print(x,"-", y,"=",  x-y)
   
   elif opert == "3":
       x = float(input("Enter the First Number : "))
       y = float(input("Enter the second Number : "))
       print(x,"*", y,"=",  x*y)
   
   elif opert == "4":
       x = float(input("Enter the First Number : "))
       y = float(input("Enter the second Number : "))
       print(x,"/", y,"=",  x/y)
   
   elif opert == "5":
       x = float(input("Enter the First Number : "))
       y = float(input("Enter the second Number : "))
       print(x,"%", y,"=",  x%y)
   
   elif opert == "6":
       x = float(input("Enter the First Number : "))
       y = float(input("Enter the second Number : "))
       print(x,"**", y,"=",  x**y)
   
   elif opert == "7":
       x = float(input("Enter the First Number : "))
       y = float(input("Enter the second Number : "))
       print(x,"//", y,"=",  x//y)
   
   elif opert == "8":
       exi = input("Do You want to Exit type Y/N : ")
       exi = exi.lower()
       if exi == "y":
           break
       elif exi == "n":
           continue
       else:
           print("Invalid Input")