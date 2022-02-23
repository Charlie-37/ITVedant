
n = int(input("Enter the number to find Factorial : "))
res = 1
for i in range(1,n+1):
    res = res * i

print(f"The Factorial of {n} is :", res)