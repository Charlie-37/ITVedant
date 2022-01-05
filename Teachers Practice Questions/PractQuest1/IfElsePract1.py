#  1) Write a program to check whether a person is eligible for voting or not. (accept age from user)

# age = int(input("Enter Your Age: "))
# if age > 18:
#     print("Eligible to Vote")
# else :
#     print(" Not Eligible to Vote")

# /*-----------------***------------------------*/

# 2) Write a program to check whether a number entered by a user is even or odd.

# print("Even ODD number check")
# num = int(input("Enter the Number : "))
# if num % 2 == 0:
#     print("The Number Is Even")
# else :
#     print("The Number is ODD ")

# /*-----------------***------------------------*/

# 3) Write a program to check whether a number is divisible by 7 or not.

# print("TO Check Number is divisible by 7")
# num = int(input("Enter the Number : "))

# if num % 7 == 0:
#     print("Number is Divisible by 7")
# else :
#     print("The number is not Divisible by  7 ")

# /*-----------------***------------------------*/

# 4) Write a program to display "Hello" if a number entered by user is a multiple of five ,otherwise print "Bye".

# print("To Check Number is Divisible By 5")
# num = int(input("Enter the number : "))
# if num % 5 == 0:
#     print("Hello")
# else :
#     print("Bye")

# /*-----------------***------------------------*/

'''5) Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :
    Unit                          Price  
  First 100 units                 no charge
  Next 100 units                 Rs 5 per unit
  After 200 units                Rs 10 per unit
  (For example if input unit is 350 than total bill amount is Rs2000)

'''

# print("Enter the Bill Unit")
# unit = float(input("Enter the Unit : "))

# if unit > 0 and unit <= 100 :
#     print("No Charge")

# elif unit > 100 and unit <= 200:
#     xfiv = unit - 100
#     yfiv = xfiv * 5
#     print("The per unit Charge is : ", yfiv)

# elif unit >200 :
#     xten = unit - 100   # cutting for NO Charges
#     yten = xten - 100   # Cutting for ( 100 units  5per unit charges)
#     zten = (100 * 5) + (yten * 10)
#     print("The per unit Charge is : ", zten)
# else :
#     print("Invalid")

    
# /*-----------------***------------------------*/
# 6) Write a program to check whether the last digit of a number (entered by user ) is divisible by 3 or not.

# print("To Check last digit is Divisible by 3 ror not")
# num = int(input("Enter a Number : "))
# xmod = num % 10;
# if xmod % 3 == 0:
#   print("Last Number is Divisible by 3")
# else:
#   print("Last number is not Divisible by 3")

# /*-----------------***------------------------*/

# 7) Write a program to determine whether a number (accepted from the user) is divisible by 2 and 3 both.

# print("To Check number is 2 or 3 ")
# num = int(input("Enter the Number : "))

# if num % 2 == 0 and num % 3 == 0:
#    print("Number is Divisible by both 2 and 3")

# elif num % 2 == 0  and num % 3 != 0:
#   print("Number is only Divisible by 2")

# elif num % 2 != 0  and num % 3 == 0:
#   print("Number is only Divisible by 3")

# else :
#   print("Number is not Divisible by any")

# /*-----------------***------------------------*/

# 8) Accept the age of 4 people and display the youngest one?

# n1 = int(input("Enter First Number : "))
# n2 = int(input("Enter Second Number : "))
# n3 = int(input("Enter 3rd Number : "))
# n4 = int(input("Enter Fourth Number : "))
# numList = [n1,n2,n3,n4]

# for i in range(0, len(numList)+1):
#   for j in range(i+1, len(numList)):
#     if numList[i] > numList[j]:
#       numList[i],numList[j] = numList[j],numList[i]
# print("The Younger Person is : ", numList[0])

# /*-----------------***------------------------*/

# 9) Accept the age of 4 people and display the oldest one.

#print("To Find the Oldest in Age")
# n1 = int(input("Enter 1st Number : "))
# n2 = int(input("Enter 2ns Number : "))
# n3 = int(input("Enter 3rd Number : "))
# n4 = int(input("Enter 4th Number : "))

# numList = [n1,n2,n3,n4]

# for i in range(0, len(numList)+1):
#   for j in range(i+1, len(numList)):
#     if numList[i] > numList[j]:
#       numList[i],numList[j] = numList[j],numList[i]
# print("The oldest age is", numList[-1])

# /*-----------------***------------------------*/

# 10) Write a program to check whether an years is leap year or not.

# year = int(input("Enter the Year : "))
# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("this is a Leap year")
#     else:
#       print("its not a leap year")  
#   else:
#     print("its a leap year")     
# else:
#  print("not a leap year")      

# /*-----------------***------------------------*/

# 11) Write a program to check whether a number entered is three digit number or not.

# print("To Check nuber length is 3 digit or not")
# num = input("Enter the number : ")
# num  = str(num)
# numList = []
# for i in range(len(num)):
  
#   numList.append(num[i])
# numLen = len(numList)
# if numLen == 3:
#   print("It is a 3 digit number ")
# else:
#   print("It is Not a 3 digit number")

# /*-----------------***------------------------*/

# 12) Write a program to check whether a person is senior citizen or not.

# print("To check person is senior Citizion or not")
# age = int(input("Enter the age : "))
# if age >= 65:
#   print("Person is Senior Citizen ")
# else :
#   print("Person is not a Senior Citizen")

# /*-----------------***------------------------*/

'''13) Write a program to accept two numbers and mathematical operators and perform operation accordingly 
	Like: Enter First Number: 7
	Enter Second Number : 9
	Enter operator : +
	Your Answer is : 16
'''

# print("Calculator")
# num1 = float(input("Enter first Number : "))
# num2 = float(input("Enter second Number : "))
# operator = input("Enter Operator : ")

# if operator == "+":
#   calc = num1 + num2
  
# elif operator == "-":
#   calc = num1 - num2

# elif operator == "*":
#   calc = num1 * num2

# elif operator == "/":
#   calc = num1 / num2

# elif operator == "%":
#   calc = num1 % num2

# else:
#   print("Invalid Input")

# print(num1, operator, num2, "=", calc)

# /*-----------------***------------------------*/
print("helo")