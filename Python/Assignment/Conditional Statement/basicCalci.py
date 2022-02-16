# //*----------Calculator------------------*//

x = float(input("Enter the First Number : "))
y = float(input("Enter the second Number : "))
opert = input("Enter the Operator : ")

if opert=="+":
   print(x, opert, y,"=",  x+y)
   
elif opert == "-":
   print(x, opert, y,"=",  x-y)

elif opert == "/":
   print(x, opert, y,"=",  x/y)

elif opert == "*":
   print(x, opert, y,"=",  x*y)

elif opert == "**":
   print(x, opert, y,"=",  x**y)

elif opert == "%":
   print(x, opert, y,"=",  x%y)

elif opert == "//":
   print(x, opert, y,"=",  x//y)

else :
   print("Invalid Operator")