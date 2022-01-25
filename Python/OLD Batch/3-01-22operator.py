
# Assignment Operator

# /-----***  ( += )    *****---------/
# a = 100
# print(a)

# a += 300
# print(a)

# /-----***  ( -= )    *****---------/
# a = 100
# print(a)

# a -= 300
# print(a)

# # /-----***  ( /= )    *****---------/
# a = 100
# print(a)

# a /= 300
# print(a)


# /-----***  ( %= )    *****---------/
# a = 100
# print(a)

# a %= 9
# print(a)


# /*-------------( Decision Making)-----------*/

# /*--------- (IF Statement )------------------*/







# /*-------WAP check number is odd or even -----*/

# numCheck = int(input("Enter the number : "))
# if numCheck % 2 == 0:
#     print("The number is EVEN")
# elif numCheck % 2 == 1 :
#     print("The number is ODD")


# /*-------WAP check mark is greater than 35  -----*/

# mark = int(input("Enter your marks :"))
# if mark > 35:
#     print("Pass")
# else :
#     print("Failed")

# /*-------WAP check age is greater than 18  -----*/

# age = int(input("Enter AGE :"))
# if age > 18:
#     print("Adult")
# else :
#     print("Child")


# /*-------WAP check username is eqal 32to "admin"  -----*/

# user  = input("Ente your username:")
# if user == "admin":
#     print("LOgin Sucessfull")
# else :
#     print("Login Failed")   

# /*-------WAP check GRADE  -----*/ 

mark = int(input("Enter the Marks"))

if mark > 35 & mark < 44 :
    print("Grade is D")
elif mark > 45 & mark < 65:
    print("Grade is C")
else :
    print("Grade is B")