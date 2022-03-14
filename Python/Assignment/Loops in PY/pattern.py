
# //*----------Star Pattern 1----*//

n = 5
for i in range(n):
    for j in range(0,i):
        print("*", end ='')
    print(" ")

print("\n")
# //*----------Star Pattern 2----*//

for i in range(n,0,-1):
    for j in range(i,1,-1):
        print("*",end='')
    print(" ")

# //*----------Star Pattern 3----*//



n = 5
for i in range(n):
    for j in range(0,i):
        print("*", end ='')
    print(" ")
for i in range(n-1,0,-1):
    for j in range(i,1,-1):
        print("*",end='')
    print(" ")


x = lambda x,y:x+y
print(x(10,20))