



def fiboS(n):
    x = 0
    y = 1
    i = 0
    str1 = ''
    while i<n:
        str1 = str1+ str(x)+ ' '
        z = x+y
        x = y
        y = z
        i=i+1
    return str1

result = fiboS(10)
print(result)

    

        
    
