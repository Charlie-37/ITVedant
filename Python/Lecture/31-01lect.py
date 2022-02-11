# x = int(input("Enter the input : "))
# //*-------------EvenODD-----------*//
# if x%2 == 0:
#     print("Number is EVEN")
# else:
#     print("Number is ODD")

# if x%3==0 and x%5==0:
#     print("Devisible by 3 and 5")
# elif x%3==0 and x%5 != 0:
#     print("number is only divisible by 3")

# elif x%3!=0 and x%5 == 0:
#     print("number is only divisible by 5")

# else:
#     print("Not Devisible by both 3 and 5")


#//*----------------------**-----------//


# year = int(input("Enter the Year : "))
# //*-----------Method 1------*/
# if (year%400) or (year%4 ==0 and year!=100):
#     print("Its a leap Year")

# else:
#     print("Its not a leap Year")


# //*------------Method 2---------*//

# if year%4 ==0:
#     if year%100==0:
#         if year%400==0:
#             print("Leap")
#         else:
#             print("Not Leap")
        
#     else:
    
#         print("Leap")
    
# else:
#     print("Not Leap")
#//*----------------------**-----------//
x = 5
if x:
    print("true")
else:
    print("false")