
# Reverse Number


def revNum(n):
    n1 = str(n)
    res = 0
    for i in range(len(n1)):
        x = n%10
        res = (res *10)+ x
        n= n//10
        
    return res



# //*---------------------**//

# Palindrome

def palNum(n):
    n1 = str(n)
    n2 = n
    res = 0
    for i in range(len(n1)):
        x = n%10
        res = (res *10)+ x
        n= n//10
        
    if res == n2:
        return print(f"{n2} is a Palindrome")
    else:
        return print(f"{n2} is Not a Paindrome")
    

# //*---------------------**-----------//

# Armstrong
#153 is Armsrong
        

def armst(n):
    n1 = n
    n2 = n
    d = 0
    res = 0
    while n!=0:
        n//=10
        d = d+1

    while n1!=0:
        rem = n1%10
        res = res+(rem**d)
        n1//=10

    if res == n2:
        return print(f"{n2} is a Armstrong Number")
    else :
        return print(f"{n2} is not a Armstrong Number")



# //*---------------------**-----------//

# Neon

def neon(n):
    sqn = n**2
    res = 0
    sq2 = sqn

    while sqn!=0:
        rem = sqn%10
        res = res+rem
        sqn//=10

    if res == n:
        return print(f"{n} is a Neon Number")
    else :
        return print(f"{n} is a Neon Number")


# //*---------------------**-----------//

# Factorial

def factN(a):
    res = 1
    
    for i in range(a):
        res = res +res *i
    return res 



        

# //*---------------------**-----------//

# STRONG

# 145 is A strong number

def strN(a):
    a1 = a
    str1 = str(a)
    res = 0
    for i in range (len(str1)):
        rem = a%10
        fact = 1
    
        for j in range(rem):
            fact = fact + fact*j
        #print(fact)
        res = res+fact
        a//=10

        if a1 == res:
            return print(f"{a1} is a Strong Number")
        else :
            return print(f"{a1} is not a Strong Number")
        

# //*---------------------**-----------//

# Fibonacci


def febo(n):
    x = 0
    y = 1
    str1 = ''
    for i in range(n):
        str1 = str1 + str(x)+" "
        z = x+y
        x = y
        y = z
    return print(str1)


# //*---------------------**-----------//

# Table

def tablm(n):
    res = 0
    str1 = ''
    for i in range(1,11):
        str1 = str1 + str(n) +"*" +str(i)+'='+str(i*n)+"\n"
        
    return print(str1)




# //*---------------------**-----------//

# Prime Number


def prnN(n):
    for i in range(2,n):
        if n%i==0:
            return print("Not Prime")
    else:
        return print("Prime")

    
