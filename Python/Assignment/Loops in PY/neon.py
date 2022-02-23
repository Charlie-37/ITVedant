

n = int(input("Enter the number to find Neon or not : "))
sq1 = n ** 2
tot = 0
print(sq1)

while sq1 !=0:
    rem = sq1 % 10 
    tot = tot + rem
    sq1 //=10


if tot == n:

    print(f"{n} is a Neon Number")
else:
    print(f"{n} is not a Neon Number")