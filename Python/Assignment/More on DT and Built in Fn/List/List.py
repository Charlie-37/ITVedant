
x = [2,4,6,8,10]

# //---------Q1--------*//
''' Q1.write a code to add a element 'eleven' , inside list at the end
output-:[2,4,6,8,10,'eleven']'''

x.append("eleven")
print("Ans 1 : ", x)


# //---------Q2--------*//
'''Q2.perform an operation to get the following output
output-: ['one', 2, 4, 6, 8, 10, 'eleven']'''

# From 1st Question the string "eleven" is alreday appended at the last

x.insert(0,"one")
print("Ans 2 : ", x)

# //---------Q3--------*//

'''Q3.perform an operation to merge the list y inside list x
y= [12,13,14]
output-: ['one', 2, 4, 6, 8, 10, 'eleven', 12, 13, 14] '''

y = [12,13,14]

x.extend(y)
print("Ans 3 : ", x)

# //---------Q4--------*//

''' Q4.perform an operation to get the following output
output-: [14, 13, 12, 'eleven', 10, 8, 6, 4, 2, 'one']  '''

x.reverse()
print("Ans 4 : ", x)

# //---------Q5--------*//

''' Q5.Perform one single operation to remove 'eleven', 10, 8 all together at once
output-: [14, 13, 12, 6, 4, 2, 'one'] '''

del x[3:6]
print("Ans 5 : ", x)

# //---------Q6--------*//

''' Q6.write a code to remove 'one' element from the list
output-: [14, 13, 12, 6, 4, 2] '''

x.pop()
print("Ans 6 : ", x)


# //---------Q7--------*//

''' Q7.write a code to get the following output
x = ["hey","there","hello","world"] '''

x[0: ] = ["hey","there","hello","world"]
print("Ans 7 : ", x)
