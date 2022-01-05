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

print("To Check last digit is Divisible by 3 ror not")
num = int(input("Enter a Number : "))
xmod = num % 10;
if xmod % 3 == 0:
  print("Last Number is Divisible by 3")
else:
  print("Last number is not Divisible by 3")

