


from tkinter import N


mylist = [11,14,5,78,45,67,9,88,10,303]

# //*---a) apply filter to create a list of palindrome numbers from mylist

def pald(n):
    n1 = n
    res = 0

    while n!=0:
        rem = n%10
        res = (res*10)+rem
        n //=10
    if res == n1:
        return res


list2=list(filter(pald,mylist))

print(list2)

# //*----b) apply filter to create a list of numbers divisible  by 3 or 5 from the mylist

def divs(n):
    if n%3==0 or n%5==0:
        return N

list3 = list(filter(divs,mylist))

print(list3)