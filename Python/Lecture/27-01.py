# #//*---------------Basic Calculator-------*//
x = float(input("Enter the first number : "))
y = float(input("Enter the Second Number : "))
opert = input("Enter the Operator : ")

if opert =="+":
        z = x+y
        print(x, opert, y, "=", z)
elif opert == "-":
    z = x-y
    print(x, opert, y, "=", z)
    
elif opert == "/":
    z = x/y
    print(x, opert, y, "=", z)

elif opert == "*":
    z = x*y
    print(x, opert, y, "=", z)

elif opert == "**":
    z = x**y
    print(x, opert, y, "=", z)

elif opert == "//":
    z = x//y
    print(x, opert, y, "=", z)

elif opert == "%":
    z = x%y
    print(x, opert, y, "=", z)
 
else:
    print("Invalid Operator")
 
 #//*---------------Comparasion Operator-------*//
# x = float(input("Enter the first number : "))
# y = float(input("Enter the Second Number : "))
# opert = input("Enter the Comparasion Operatot : ")

# if opert == "<":
#     if x < y :
#         print("True")
#     else:("False")

# elif opert == ">":
#      if x > y :
#         print("True")
#      else:("False")

# elif opert == ">=":
#      if x >= y :
#         print("True")
#      else:("False")

# elif opert == "<=":
#      if x <= y :
#         print("True")
#      else:("False")
     
# elif opert == "==":
#      if x == y :
#         print("True")
#      else:("False")

# elif opert == "!=":
#      if x != y :
#         print("True")
#      else:("False")
    

# else : ("Invalid Operator")
    

#//*---------------Logical Operator-------*//

# # //*----------AND OP-------------**/
# x = float(input("Enter the first number : "))
# y = float(input("Enter the Second Number : "))

# if x>10 and y>10:
#     print("true")
# else:
#     print("False")


# # //*----------OR OP-------------**/
# x = float(input("Enter the first number : "))
# y = float(input("Enter the Second Number : "))

# if x>10 or y>10:
#     print("true")
# else:
#     print("False")

# //*----------NOT OP-------------**/
# x = float(input("Enter the first number : "))
# y = float(input("Enter the Second Number : "))

# if not(x>10 and y>10):
#     print("true")
# else:
#     print("False")

# //*------------------Greater --------------*//
# x = float(input("Enter X : "))
# y = float(input("Enter Y : "))

# if x > y:
#     print(x, "X is Greater")
# elif x < y :
#     print(y, "Y is Greater")
# elif x == y :
#     print("Both are Equal")
# else:
#     print("Invalid Input")

