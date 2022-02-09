# //* ----------------Imaginary (Complex Numbar)---------*//

# x = 3 + 4j
# print(x.real)
# print(x.imag)

# # //*--------------Tuple---------*//
# y = ("cat", "Dog", "Whale")
# print("It is a Tuple", y)

# # //*--------------List---------*//
# z = ["Green", "Blue", "Red"]
# print("It is a List", z)

# # //* ----------------Dictonary---------*//

# x = {
#     'a':10,
#     'b': 20, 
#     'a' : 30
#     }

# print("It is a Dictonary", x)

# # //* ----------------Set---------*//

# a = {"Apple", 2, True}
# print("It is a SET", a)

# # //* ----------------MultiLine String---------*//
# x = '''hello
# Line 2
# Line 3'''
# print(x)


# //* ----------------String Operation---------*//

# //* ----------------Concat---------*//

# x = "Sunil"
# y = "Bhave"
# z = x + " " + y
# print(z)

# //* ----------------Reeplication---------*//

# x = "Sunil"
# y = "Bhave"
# z = x + " " * 3
# print(z)

# a = (x + " ") * 3
# print(a)

# //* ----------------Indexing---------*//

# x = "I love Python Program"
# z = x[7]+x[8]+x[9]+x[10]+x[11]+x[12]
# y = x[-19]+x[-18]+ x[-17]+x[-16] +" "+ x[-14]+x[-13]+x[-12]+x[-11]+x[-10]+x[-9]

# print(z)
# print(y)


# # //* ----------------Slicing---------*//

# x = "I love Python Program"
# z = x[7:13]
# print(z)

# a = x[ 7: ]
# print(a)

# y = x[ : :-1]
# print(y)

# b = x[: : 2]
# print(b)

# c = x[ : :-3]
# print(c)

# # //* ----------------Tuple String Opert---------*//

# x = (1,2,3,4,5,6,7)
# y = (11,12,13,14,15)
# print("Concatinating")
# z = x+y
# print(z)

# print("Indexing")
# y = z[2]
# print(y)

# print("Slicing")
# a = z[2 : 11 : 2]
# print(a)

# print("Replicating")
# b = z*3
# print(b)



# //* ---------------List String Opert---------*//

# x = [1,2,3,4,5,6,7]
# y = [11,12,13,14,15]

# print("Concatinating")
# z = x+y
# print(z)

# print("Indexing")
# y = z[9]
# print(y)

# print("Slicing")
# a = z[0 : 15 : 3]
# print(a)

# print("Replicating")
# b = z*5
# print(b)




# //* ---------------Leap---------*//

# x = int(input("Enter the number : "))

# if x%4 == 0:
#     if x%100 ==0:
#         if x%400 ==0:
#             print("Leap year")
#         else:
#             print("Not a leap")
#     else:
#         print("Leap year")
# else:
#     print("Not a aleap year");



# # //* ---------------Factorial---------*//
# x = int(input("Enter the number : "))
# fact = 1
# res = 1

# while fact <= x:
#     res = res*fact
#     fact+=1
# print(res)

# # //* ---------------Slicing n rev---------*//

# n = input("Enter the sentence : ")
n = "My name is sunil"
o = n.split()
#print(o)
z = n[ : : -1]
k =[]
for i in range(0, len(o)):
    a= o[i]
    x = a[ : : -1]
    print(x, end=" ")
    



