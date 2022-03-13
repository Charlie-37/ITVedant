
# //*-------Program to find 2nd Highest value
h1,h2 = -999999,-999999

list1 = [12,925,35,15,7774,4]

for i in list1:
    if i>=h1:
        h1,h2=i,h1
    elif i>h2:
        h2=i


print(list1)
print('Heighest Value in the list is :',h2)