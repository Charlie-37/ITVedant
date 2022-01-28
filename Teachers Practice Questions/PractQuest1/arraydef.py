# 1.Take a number from the user, check if it is prime or not  using a break statement.

# x = int(input("Enter the number : "))
# flag = False

# # prime numbers are greater than 1
# if x > 1:
#     # check for factors
#     for i in range(2, x):
#         if (x % i) == 0:
#             # if factor is found, set flag to True
#             flag = True
#             # break out of loop
#             break

# # check if flag is True
# if flag:
#     print(x, "is not a prime number")
# else:
#     print(x, "is a prime number")

#  //*-------------------**-----------------------------//

''' 2.	Take a number from the user, check if it is prime or not  without using a break statement. '''

# x = int(input("Enter the number : "))
# flag = False

# # prime numbers are greater than 1
# if x > 1:
#     # check for factors
#         if (x % i) == 0:
#             # if factor is found, set flag to True
#             flag = True
            

# # check if flag is True
# if flag:
#     print(x, "is not a prime number")
# else:
#     print(x, "is a prime number")

#  //*-------------------**-----------------------------//

# 3.	Create a function which accept number or check it prime or not using recursion without using loop

# def chkprime(n,i):
#     while i<n:
#         if n%i==0:
#             return False
#         else:
#             i+=1
#             chkprime(n,i)
#     return True
# n = int(input("Enter the number : "))

# if chkprime(n,2):
#     print("Number is prime")
# else:
#     print("Number is not prime")


#  //*-------------------**-----------------------------//

# 4.	Create a function which accept any 5 element and print in ascending or descending

# a = int(input("Enter the Number : "))
# b = int(input("Enter the Number : "))
# c = int(input("Enter the Number : "))
# d = int(input("Enter the Number : "))
# e = int(input("Enter the Number : "))
# numList=[]

# opert = input("Enter 1 for Ascending or 2 for Descending : ")

# num = [a,b,c,d,e]


# def asc(num):
#     if opert=="1":
#         for i in range(5):
            
#             for j in range(i+1, 5):
#                if(num[i]>num[j]):
#                    temp = num[i]
#                    num[i]=num[j]
#                    num[j] = temp
#     elif opert == "2":
#         for i in range(5):
#             for j in range(i+1, 5):
#                  if(num[i]<num[j]):
#                       temp = num[i]
#                       num[i]= num[j]
#                       num[j]=temp

# asc(num)
# print(num)


#  //*-------------------**-----------------------------//

# 5.	Create a function which accepts any array with five number and print largest number from array.

# a = int(input("Enter the number : "))
# b = int(input("Enter the number : "))
# c = int(input("Enter the number : "))
# d = int(input("Enter the number : "))
# e = int(input("Enter the number : "))

# num = [a,b,c,d,e]

# def larg(num):
#     for i in range(5):
#         for j in range(i+1, 5):
#             if(num[i]>num[j]):
#                 temp = num[i]
#                 num[i] = num[j]
#                 num[j] = temp

# larg(num)
# print(num[-1])



#  //*-------------------**-----------------------------//

# 6.	Create a function which accepts any array with five numbers and prints the largest odd number from the array.

# a = int(input("Enter the number : "))
# b = int(input("Enter the number : "))
# c = int(input("Enter the number : "))
# d = int(input("Enter the number : "))
# e = int(input("Enter the number : "))

# num = [a,b,c,d,e]

# newnum=[]

# def largodd(num):

#     for k in (num):
#         if(k%2 != 0):
#             newnum.append(k)
            
#     sort(newnum)
            

# def sort(newnum):
#     for i in range(len(newnum)):
#         for j in range(i+1, len(newnum)):
#             if(newnum[i]>newnum[j]):
#                 temp = newnum[i]
#                 newnum[i] = newnum[j]
#                 newnum[j] = temp

# largodd(num)

# print("The Largest ODD number is : ", newnum[-1])


#  //*-------------------**-----------------------------//

# 7.	Create a function which accepts any String or print in reverse order. Eg. coder      O.P: redoc
