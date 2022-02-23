from re import I


n = int(input("Enter the number to find Table : "))
i = 1
while i <11:
    res = n * i
    print(n, "*", i, "=", res)
    i+=1
