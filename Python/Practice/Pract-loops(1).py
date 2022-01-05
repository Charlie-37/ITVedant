# /*---------------Factorial using loop----------*/
# n = int(input("Enter num : "))
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i
# print("Factorial is : ", fact)


# /*---------------sum of n natural number-----------*/

# num = int(input("Enter the number : "))
# res = 0

# for i in range(num +1):
#     res = res + i
#print("the sum of n interger is : ", res)


# /*---------------sum of n natural number-----------*/
# n = 5
# for i in range(0, n+1):
#     for j in range(0, i+1):         
#      print("*", end='')
#     print('')

# # /*---OUTPUT---*/
#          *
#          ** 
#          ***
#          ****
#          *****
#          ******
    

# /*---------------sum of n natural number-----------*/
# n = 5
# for i in range(0, n+1):
#     for j in range(0, i):
#      print(i, end='')
#     print('')
    
 # /*---OUTPUT---*/
#     1
#     22
#     333
#     4444
#     55555

# /*---------------sum of n natural number-----------*/
# n = 5
# for i in range(0, n+1):
#     for j in range(1, i+1):
#      print(j, end='')
#     print('')

 # /*---OUTPUT---*/
#      1
#      12
#      123
#      1234
#      12345

# /*---------------sum of n natural number-----------*/
# n = 5
# b = 0
# for i in range(n, 0, -1):
#     for j in range(0, i):
#      print(i, end='')
#     print('')


 # /*---OUTPUT---*/
 #     55555
 #     4444
 #     333
 #     22
 #     1


 # /*---------------sum of n natural number-----------*/
# n = 5

# for i in range(n, 0, -1):
#     for j in range(1, i+1):
#      print(j, end='')
#     print('')

# /*---OUTPUT---*/

#      12345
#      1234
#      123
#      12
#      1


 # /*---------------sum of n natural number-----------*/
# n = 5

# for i in range(n, 0, -1):
#     for j in range(i, 0, -1):
#      print(j, end='')
#     print('')

# /*---OUTPUT---*/

#      54321
#      4321
#      321
#      21
#      1


 # /*---------------sum of n natural number-----------*/
# n = 5
# for i in range(1, n+1):
#     for j in range(i, 0, -1):
#      print(j, end='')
#     print('')

# /*---OUTPUT---*/

#      1
#      21
#      321
#      4321
#      54321



