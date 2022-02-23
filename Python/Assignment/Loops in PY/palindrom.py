
n = int(input("Enter the number to check Palindrome or not : "))
n1 = n
rev = 0
while n!=0:
    rem = n %10
    rev = (rev *10)+rem
    n//=10

if rev == n1:
    print(f"{n1} Is a Palindrome")
else:
    print(f"{n1} Is not a Palindrome")

