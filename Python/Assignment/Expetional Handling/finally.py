
# //*---Finally in Python---*/
##def checkp(x):
##     try:
##         
##         
##         if x > 1:
##            print("x is greater than 1")
##     except:
##        print("Something went wrong")
##
##     finally:
##        print("The try...except block is finished")
##
##
### If X = 3
##checkp(3)



# //*-----------Raise----------*//

##x = 101
##
##if x > 100:
##  raise Exception("Error, Number is above 100")


# //*------multiple Except-------*//

##try:
##    a = int(input("Enter value of a: "))
##    b = int(input("Enter value of b: "))
##    c = a/b
##    print("a/b = ", c)
##except ValueError:
##    print("Invalid Input, Value must be Integer")
##    
##except ZeroDivisionError:
##    print("Zero Division Error")
##
##


try:
    a = int(input("Enter value of a:"))
    b = int(input("Enter value of b:"))
    c = a / b
    print("a/b =", c)

except ZeroDivisionError:
    print("Can't divide by zero")
else:
    print("We are in else block ")
