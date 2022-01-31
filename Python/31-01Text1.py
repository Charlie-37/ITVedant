x = float(input("Enter the First Number : "))
y = float(input("Enter the Second Number : "))
opert = input("Enter the operator : ")

if opert == "+":
    z = x+y
    print(x, opert, y, "=", z)

elif opert == "-":
    z = x - y
    print(x, opert, y, "=", z)

elif opert == "/":
    z = x / y
    print(x, opert, y, "=", z)

elif opert == "*":
    z = x * y
    print(x, opert, y, "=", z)

elif opert == "%":
    z = x % y
    print(x, opert, y, "=", z)

elif opert == "//":
    z = x // y
    print(x, opert, y, "=", z)

elif opert == "**":
    z = x ** y
    print(x, opert, y, "=", z)

else :
    print("Invalid Input")