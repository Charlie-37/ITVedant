
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


# /*--------------Pattern 3----------*/

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

# /*--------------Pattern 3----------*/

n = 5
for i in range(0, n+1):
    for j in range(n, i,-1):
        print(j, end='')
    print("")