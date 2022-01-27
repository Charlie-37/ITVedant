
# /*--------------Pattern 1----------*/
# n = 5

# for i in range(0, n+1):
#     for j in range(1, n+1):
#      print(j, end='')

#     print("")

# OUTPUT

#  12345
#  12345
#  12345
#  12345
#  12345
#  12345

# /*--------------Pattern 2----------*/
# n = 5
# for i in range(0, n+1):
#     for j in range(n, 0, -1):
#         print(j, end='')
#     print("")

# OUTPUT

# 54321
# 54321
# 54321
# 54321
# 54321
# 54321


# /*--------------Pattern 3----------*/
# n = 5
# for i in range(0, n+1):
#     for j in range(1, i+1):
#         print(j, end='')
#     print("")

# OUTPUT 

#  1
#  12
#  123
#  1234
#  12345


# /*--------------Pattern 4----------*/

# n = 5
# for i in range(0, n+1):
#     for j in range(n, i, -1):
#         print(j, end='')
#     print("")

# OUTPUT 

#  54321
#  5432
#  543 
#  54  
#  5 

# /*--------------Pattern 5----------*/

# n = 5
# for i in range(0, n):
#     for j in range(0, i):
#         print(" ", end='')
#     for k in range(0, n-i):
#         print(k+1, end='')
#     print("")

# OUTPUT 

'''
12345
 1234
  123
   12
    1

'''
# /*--------------Pattern 6----------*/

# n = 5
# for i in range(0, n+1):
#     for j in range(1, i+1):
#         print(j, end='')
#     print("")

# OUTPUT 

'''
1
12
123
1234
12345

'''

# /*--------------Pattern 6----------*/

# n = 5
# k = ord("A")
# for i in range(0, n):
#     for j in range(1, n+1):
#         print(chr(k), end=" ")
#         k+=1
#     print("")

# OUTPUT

'''
A B C D E 
F G H I J 
K L M N O 
P Q R S T 
U V W X Y 

'''

# /*--------------Pattern 7----------*/

# n = 5
# k = ord("A")
# for i in range(0, n):
#     for j in range(1, n+1):
#         print(chr(k), end=" ")
#         k+=1
#     k = ord("A")
#     print("")

# OUTPUT 

'''
A B C D E 
A B C D E 
A B C D E 
A B C D E 
A B C D E 
'''

# /*--------------Pattern 8----------*/

# n = 5
# k = ord("A")
# for i in range(0, n+1):
#     for j in range(1, i+1):
#         print(chr(k), end=" ")
#         k+=1
#     k = ord("A")
#     print("")

# OUTPUT

'''
A 
A B 
A B C 
A B C D 
A B C D E 
'''

# /*--------------Pattern 9----------*/

# n = 5
# k = ord("A")
# for i in range(0, n):
#     for j in range(0, i+1):
#         print(chr(k), end=" ")

#     k+=1
#     print("")

#  OUTPUT

'''
A 
B B       
C C C     
D D D D   
E E E E E 
'''

# /*--------------Pattern 10----------*/

# n = 5
# k = ord("A")
# k+=4
# for i in range(0, n):
#     for j in range(n, i, -1):
#         print(chr(k), end=" ")

#         k-=1
#     k = ord("A")
#     k+=4
#     print("")

#  OUTPUT

'''
E D C B A 
E D C B 
E D C 
E D 
E 
'''


# /*--------------Pattern 11----------*/
# n = 5
# count = 1
# for i in range(1, n+1):
#     for j in range(0, n):
#         print(count%2, end=" ")
#         count+=1
    
#     if i%2==0:
#         count =1
#     else:
#         count = 0

#     print("")

# OUTPUT 

'''
1 0 1 0 1 
0 1 0 1 0 
1 0 1 0 1 
0 1 0 1 0 
1 0 1 0 1 
'''

# /*--------------Pattern 12----------*/
# n = 5
# for i in range(0, n):
#     for j in range(n,i,-1):
#          print("*", end=" ")

#     print("")

# OUTPUT 

'''
* * * * * 
* * * * 
* * * 
* * 
* 
'''


# /*--------------Pattern 13----------*/
# n = 5
# for i in range(0, n):
#     for j in range(n, i,-1):
#          print(j-i, end=" ")

#     print("")

# OUTPUT 

'''
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1 
'''

# /*--------------Pattern 14----------*/

# n = 5
# for i in range(0, n):
#     for j in range(n-1, i,-1):
#          print(" ", end=" ")
#     for k in range(i,-1,-1):
#         print(k+1, end=" ")

#     print("")

# OUTPUT 

'''
        1 
      2 1 
    3 2 1 
  4 3 2 1 
5 4 3 2 1 
'''

# /*--------------Pattern 15----------*/

# n = 5
# for i in range(0, n):

#     if i%2 ==0 :
#          for j in range(0,n):
#              print("*", end="")
#     else:
#         for j in range(0,n,+2):
#              print("*", end=" ")

#     print("")

# OUTPUT

'''
*****
* * * 
*****
* * * 
*****
'''

# /*--------------Pattern 16----------*/
# n = 6
# for i in range(1, n):
#   for j in range(i, 0, -1):
#     print(j, end='')
#   print(" ")

#OUTPUT 

'''
1 
21    
321   
4321  
54321 
'''

# /*--------------Pattern 17----------*/
for i in range(6,0,-1):
  for space in range(6,i,-1):
    print(" ",end="")
  for j in range(1,i+1):
    print(j,end=" ")
  print()

#OUTPUT 

'''
1 2 3 4 5 6 
 1 2 3 4 5 
  1 2 3 4
   1 2 3
    1 2
     1
'''