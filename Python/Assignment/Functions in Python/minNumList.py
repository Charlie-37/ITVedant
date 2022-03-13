# //*----- Minimum from the list

n = 9999999

list1=[12,53,6,23,6,87,1,-78]

for i in list1:
    if i<n:
        n = i

print("Minimum number of the List is :",n)