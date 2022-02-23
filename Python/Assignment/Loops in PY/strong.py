
n = int(input("Enter the number to find Strong Or Not : "))
n1 = n
res = 0


# While to take out the last number
while n!=0:
    rem = n%10
    f = 1
    fact = 1
    # While to find the factorial that last number
    while f <= rem:
        fact = fact * f
        f+=1
    # Adding the factorial
    res = res + fact
    n//=10

if res == n1:
    print(f"{n1} is a Strong Number.")
else:

    print(f"{n1} is not a Strong Number. ")

