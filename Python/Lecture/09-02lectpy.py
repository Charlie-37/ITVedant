
# //* ----Word----*//
n = "i LoVe PYtHoN pRogRaMminG"

# //*-------- String lower()-------------*//
# //* Convert the string into Lower Case

#  # //*----Reasigning----------*//
# # n = n.lower()
# # print(n)

x = n.lower()
print(x)



# //*-------- String Upper()-------------*//
# //* Convert the string into Upper case

# //*----Reasigning----------*//
# n = n.upper()
# print(n)

# y = n.lower()
# print(y)

# //*-------- String title()-------------*//
# //* Convert the Starting letter of Each Word to Capital Letter and other words to Lower Case
# print(n)
# a = n.title()
# print(a)

# //*-------- String capitalize()-------------*//
# //* Convert the Starting letter of the sentence to Upper case and other to lower case
# print(n)
# b = n.capitalize()
# print(b)

# //*-------- String swapcase()-------------*//
# //* Swap the letter from Upper case to Lower Case and Vice Versa

# c = n.swapcase()
# print(n)
# print("By Swap case")
# print(c)


# //* -----New Word--------*//

m = "I love python programming and python"


# //*-------- String find()-------------*//
# //* Finds the index number of given value

# d = m.find("and python")
# print(d)


# //* Mixing String Functions (str.find() inside str[](Slicing))

# e = m[m.find("pr"): m.find(" a")]
# print(e)
# //* OUTPUT : 
# programming

# f = m[m.find("py"): m.find(" a")]
# print(f)
# //* OUTPUT :
# python programming




# //*-------- String count()-------------*//
# //* Gives the count of repeted words
# h = m.count("python")
# print(h)


# //*-------- String replace()-------------*//
# //* Replace the word in a string 

# i = m.replace("python", "Golang")
# print(i)


# //*-------- String formatting()-------------*//
# //* Adding variabke or specific value between the statement

# //*-----Type 1------**/
# st1 = "My name is {}, my age is {}".format("Sunil",23 )
# print(st1)

# //*-----Type 2------**/
# st2 = "My name is {name}, my age is {age}".format(age=27, name="Sneha" )
# print(st2)

# //*-----Type 2------**/
# name = "Sneha"
# age = 23
# st3 = f"My name if {name}, my age is {age}"
# print(st3)


# //*-------- String split()-------------*//
# //* Splits the string and adds into the List, By default the splitting condition is Space, but it can be coustomize

# x = "Hello World, Welcome to Python Programming"
# y = "sunilbhave36@gmail.com"

# sp1 = x.split()
# sp2 = y.split("@")
# print(sp1)
# print(sp2)

# print("The domain is : ", sp2[-1])

# //* ----Append() adds the value at the last of the list
# str3=["I", "Love", "Python"]
# str3.append("Language")
# print(str3)

# # //*-------- String join()-------------*//
# # //* Join() joins the list taking " "(space) as a medium of each element of the list.
# x = " ".join(str3)
# print(x)


# //* -------------LIST--------------**/
x = [1,3,5,7,9]
# # //*---------Append()---------//
# # //* Adds value at the last in the list
# x.append(10)
# print(x)

# # //*--------Insert()-------------//
# # //* Adds value at the specific position in the list

# x.insert(1,"two")
# print(x)

# # //*--------Extend()-------------//
# y = [10,12,13,14]
# x.extend(y)
# print(x)

# //* Experiment Difference between append and extend
x.append(" and so on append")
x.extend("and so on extend")

print(x)

x = "I love Python, Python is best"
y = x.find("is")
print(y)
