n = 7546

rev = 0
while n!=0:
    rem = n %10
    rev = (rev *10)+rem
    n//=10

print(rev)