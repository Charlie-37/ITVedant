
# /*---Table----------*//

##n = 8
##
##for i in range(1,11):
##    res = i * n
##    print(n, "*", i, "=", res)
##


# //*----- fact-----*//

##res = 1
##fact = 1
##n = 5
##
##for i in range(1, n+1):
##    res = res * i
##    print(res)
##


# //*----Febonacii------*//

##x = 0
##y = 1
##n = 10
##for i in range(0, n):
##    print(x)
##    z = x+y
##    x = y
##    y = z
##


# //*-NUM REVERSE and palindrom------*//

##n = int(input("Enter the number : "))
##pal = n
##x  = str(n)
##
##res = 0
##for i in range(0, len(x)):
##    rem = n%10
##    res = (res *10)+rem
##    n//=10
##    
##print(res)
##
##if pal == res:
##    print("Palindrom")
##else:
##    print("Not Palindrom")


# /*-----Max list------*//

x = [1,5,25,1,5,0,1]
mint = -9999999

for i in range(0, len(x)):
    if x[i]>mint:
        mint = x[i]
print(mint)



















    
