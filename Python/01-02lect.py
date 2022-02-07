# //*-------------Even ODD-------*//

# x = int(input("Enetr the number : "))

# if x % 2 == 0:
#     print("Number is Even")
# else :
#     print("Number is ODD")


#//*---------------------Leap Year--------------**/

# x = int(input("Enter the Year"))

# if x%4 ==0:
#     if x%100 ==0:
#         if x%400 ==0:
#             print("Leap Year")
#         else:
#             print("Not A Leap Year")
#     else:
#         print("Leap Year")
# else:
#     print("Not A laep Year")
 
 
#//*---------------------****-----------------*//
#//*---------------------Print(1 to 10)-----------------*//

# for i in range(10, 0, -1):
#     print(i)

# x = 10
# while x>0:
#     print(x)
#     x-=1


#//*---------------------****-----------------*//
#//*---------------------Factorial-----------------*//

# x = int(input("Enter the Numbar : "))
# res = 1
# fact = 1

# while fact<=x:
#     res = res * fact
#     fact +=1
# print(res)


#//*---------------------****-----------------*//
#//*---------------------Addition Till N Number-----------------*//

# x = int(input("Enter the Numbar : "))

# res = 0
# n = 1

# while n<=x:
#     res = res + n
#     n = n+1
# print(res)


#//*---------------------****-----------------*//


x = 0
while x<=10:
    x = x+1
    if(x == 5):
        break
    print(x)