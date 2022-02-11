# //*------------ Console Base Calc. ------------------**//

while(True):
    print("\n * Welcome To My Calculator * \n ")
    print("Please Select a Choise ")
    print("1 : Addition ")
    print("2 : Substraction")
    print("3 : Devision ")
    print("4 : Multiplication ")
    print("5 : Modulus ")
    print("6 : Power ")
    print("7 : Floor ")
    print("8 : Exit ")
    
    c = input("Enter Your Choice : ")

    if c == "1":
        x = float(input("Enter the first number : "))
        y = float(input("Enter the second number : "))
        print(x, "+", y, "=", x+y )

    elif c == "2":
        x = float(input("Enter the first number : "))
        y = float(input("Enter the second number : "))
        print(x, "-", y, "=", x-y )

    elif c == "3":
        x = float(input("Enter the first number : "))
        y = float(input("Enter the second number : "))
        print(x, "/", y, "=", x/y )

    elif c == "4":
        x = float(input("Enter the first number : "))
        y = float(input("Enter the second number : "))
        print(x, "*", y, "=", x*y )

    elif c == "5":
        x = float(input("Enter the first number : "))
        y = float(input("Enter the second number : "))
        print(x, "%", y, "=", x%y )

    elif c == "6":
        x = float(input("Enter the first number : "))
        y = float(input("Enter the second number : "))
        print(x, "**", y, "=", x**y )

    elif c == "7":
        x = float(input("Enter the first number : "))
        y = float(input("Enter the second number : "))
        print(x, "//", y, "=", x//y )

    elif c == "8":
        x = input("Are You Sure Y/N : ")
        x = x.upper()
        
        if x == "Y":
            break
        elif x == "N":
            continue
        else:
            print("Invalid Number")

    else:
        print("Invalid Number")