# '''5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. Go to the editor
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2'''

# list1 = ['abc', 'xyz', 'aba', '1221']
# count = 0
# for i in list1:
#     if len(i) >= 2: 
#         if i[0] == i[-1]:
#             count +=1

# print(count)


# //*-----------------------------------------------------**------------------------------------------------//

'''6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. Go to the editor
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
'''

# l1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# def last(l1):
#     return l1[-1]

# print(sorted(l1,key=last))

    
# //*-----------------------------------------------------**------------------------------------------------//

'''7. Write a Python program to remove duplicates from a list. Go to the editor'''

# l1 = [1,5,2,7,6,3,5,2,9,6,9]

# l2 = set(l1)
# l2 = list(l2)
# print(l2)

# //*-----------------------------------------------------**------------------------------------------------//

'''14. Write a Python program to print the numbers of a specified list after removing even numbers from it'''

# l1 = [1,5,2,7,6,3,5,2,9,6,9]
# l2 = []

# for i in l1:
#     if i%2 != 0:
#         l2.append(i)
# print(l2)

# //*-----------------------------------------------------**------------------------------------------------//
'''35. Write a Python program to create a list by concatenating a given list which range goes from 1 to n. Go to the editor
Sample list : ['p', 'q']
n =5
Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']'''

# l1 = ['p', 'q']
# n = 5
# i = 1
# l2 = []

# for i in range(1,n+1):
#     for j in l1:
#         l2.append(j+str(i))
# print(l2)



# //*-----------------------------------------------------**------------------------------------------------//

'''39. Write a Python program to convert a list of multiple integers into a single integer. Go to the editor
Sample list: [11, 33, 50]
Expected Output: 113350'''

# l1 = [11, 33, 50]
# st1 = ''
# l2 = []
# for i in l1:
#     l2.append(str(i))

# x = ''.join(l2)
# print(x)
# //*-----------------------------------------------------**------------------------------------------------//



''' Write a Python program to convert list to list of dictionaries. Go to the editor
Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]'''

# l1 = ["Black", "Red", "Maroon", "Yellow"]
# l2 = ["#000000", "#FF0000", "#800000", "#FFFF00"]
# clist = []
# for i,j in zip(l1,l2):
#     clist.append({"color name" : i, 'color code' : j})

# print(clist)
# //*-----------------------------------------------------**------------------------------------------------//

# '''51. Write a Python program to split a list every Nth element. Go to the editor
# Sample list: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# Expected Output: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]'''

# l1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']

# def ld(S,step):
#     return[S[i::step] for i in range(step)]

# print(ld(l1,3));
# //*-----------------------------------------------------**------------------------------------------------//

'''72. Write a Python program to flatten a given nested list structure. Go to the editor
Original list: [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
Flatten list:
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]'''


# l1 = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
# l2 = []
# for i in l1:
#     if type(i) == int:
#         l2.append(i)
#     else:
#         for j in i:
#             l2.append(j)
    
# print(l2)

# //*-----------------------------------------------------**------------------------------------------------//


