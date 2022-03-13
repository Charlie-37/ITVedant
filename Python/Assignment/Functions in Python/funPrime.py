
# //*------Function to Check Prime Number---///

def primeChek(n):

    for i in range(2,n):
        if n % i ==0:
            return print(f"{n} is Not a Prime Number")
    else:
        return print(f"{n} is a Prime Number")


n = int(input("Enter the Number to Check Prime : "))
primeChek(n)