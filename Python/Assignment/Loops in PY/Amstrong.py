n =  int(int("Enter the number to check Armstrong or Not : "))
n1 = n
n2 = n
tot = 0
l = 0

while n!=0:
    n = n//10
    l = l+1


while n1!=0:
    rem = n1 %10
    tot = tot + (rem ** l)
    n1//=10

if tot == n2:
    print(f"{n2} is a Armstrong No.")
else:
    print(f"{n2} is a not Armstrong No.")

