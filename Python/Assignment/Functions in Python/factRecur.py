
# //*----Factorial using Recurssion----*//


def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)

n = int(input("Enter the number to find Factorial : "))
print(f"Factorial of {n} is: ",fact(n))