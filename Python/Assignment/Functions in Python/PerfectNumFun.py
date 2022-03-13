
# //*-------Function for Perfect Number----//

def perfNum(n):

    sum = 0
    for i in range(1,n):
        if n % i==0:
            sum = sum+i
    
    if sum==n:
        return print(f"{n} is a Perfect Number")
    else:
        return print(f"{n} is not a Perfect Number")

n = int(input("Enter a Positive Interger to Check Perfect Number : "))
perfNum(n)