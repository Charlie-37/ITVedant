
x ="i LoVe pYtHoN PrOGrAm"

# //*---------Q1---------*//
'''Q1.write a code to get the following ouput....
output-: 'I love python program' '''

y = x.capitalize()
print("Ans 1 : ", y)

# //*---------Q2---------*//
''' Q2.write a code to get the following ouput....
output-: 'I Love Python Program' '''

altc = x.title()
print("Ans 2 : ", altc)

# //*---------Q3---------*//
''' Q3.write a code to get the following ouput....
output-: 'i love python program' '''

lowc = x.lower()
print("Ans 3 : ", lowc)

# //*---------Q4---------*//
''' Q4.write a code to get the following ouput....
output-: 'I LOVE PYTHON PROGRAM  '''

uppc = x.upper()
print("Ans 4 : ", uppc)

# //*---------Q5---------*//
''' Q5.write a code to get the following ouput....
output-: ['i', 'LoVe', 'pYtHoN', 'PrOGrAm'] '''

swpl = x.split()
print("Ans 5 : ", swpl)

# //*---------Q6---------*//
''' Q6.use format method to inject the following name and age variable in given variable named string 
name="python"
age=30
string="my name is {} and my age is {}"
output-: 'my name is python and my age is 30 '''

name1 = "python"
age1 = 30
str1 = f"my name is {name1} and my age is {age1}."
print("Ans 6 :", str1)

# //*---------Q7---------*//
''' Q7.write a code to retrieve the word 'pYtHoN' by using slicing from variable x
output-: 'pYtHoN' '''

slic = x[x.find("p"): x.find("oN")+2]
print("Ans 7 : ",slic)
