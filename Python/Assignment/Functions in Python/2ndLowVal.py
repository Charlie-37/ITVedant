
#//*----Program to find 2nd Lowest value---*//


list1 = [12,6,69,32,8]

for i in range(0, len(list1)+1):
    for j in range(i+1, len(list1)):
        if list1[i]>list1[j]:
            list1[i],list1[j] = list1[j],list1[i]

print("Using Bubble Sort", list1[1])




a = 999999
b = 999999

for x in list1:
    if x <= a:
        a,b = x,a
    elif x<b:
        b = x

print("Using Basic Methid", b)

