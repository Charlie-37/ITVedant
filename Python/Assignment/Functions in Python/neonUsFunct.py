

def neonN(n):

    sqN= n**2
    res = 0

    while sqN!=0:
        rem = sqN%10
        res = res + rem
        sqN //=10

    if res == n:
        return print(f"{n} is a Neon Number.")
    else:
        return print(f"{n} is not a Neon Number.")


n = int(input("Enter the Number to Check Neon Number : "))
neonN(n)

