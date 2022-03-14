
# //*----------zip()------------*//

list1=[1,2,3,4]
list2=["apple","banana","orange","mango"]

result = zip(list1,list2)
result_set = set(result)
print(result_set)
print("-*"*30,"\n")

# //*----------abs()------------*//

n1 = -45
n2 = -72.33
n3 = 7 + 2j

print(f"Absolute of {n1} is :", abs(n1))
print(f"Absolute of {n2} is :", abs(n2))
print(f"Magnitude of {n3}is :", abs(n3))
print("-*"*30,"\n")


# //*----------round()------------*//

m1 = 56.7678773
m3 = 64.1232221
m2 = 98.09939

print(f"Absolute Round of {m1} is :", round(m1))
print(f"Absolute Round of {m3} is :", round(m3))
print(f"Round of {m2} is :", round(m2,3))
print("-*"*30,"\n")

# //*----------pow()------------*//

x1 = 2
print(f"Power of {x1} to 3 is :",pow(x1,4))