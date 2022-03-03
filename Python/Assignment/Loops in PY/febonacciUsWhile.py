n = int(input("Enter the number to Find Febonacci : "))
i = 0
x=0
y=1
print(f"Febonacci till {n} :s" )
while i<n:
    print(x, end = " ")
    z = x + y
    x = y
    y = z

    i+=1
