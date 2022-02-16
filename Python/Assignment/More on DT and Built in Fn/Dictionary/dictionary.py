d = {'a':10,'b':30,'c':50,'d':100}

# //*---------Q1--------------*//
''' Q1.write a code to update the value of key 'b' to 300
output-: {'a':10,'b':300,'c':50,'d':100}  '''

d.update({"b" : 300})
print(d)

# //*---------Q2--------------*//

''' Q2.write a code to check if key 'e' is present in dictionary d
if it 'e' is not present in d, then it should return 'e key does not exist'
output-: 'e key does not exist '''

e = d.get('e','Does not exist')
print(e)


# //*---------Q3--------------*//
''' Q3.write a code to add new key,value  i.e 'e',600 respectively inside dictionary d
output-: {'a':10,'b':300,'c':50,'d':100,'e':600} '''

d.setdefault("e",600)
print(d)

# //*---------Q4--------------*//
''' Q4.write a code to display all the values from the dictionary
output-: dict_values([10, 300, 50, 100, 600])'''

q = d.values()
print(q)

# //*-------Q5--------*//

''' Q5.write a code to merge the dictionary x inside dictionry d
x = {'i':11,'j':12,'k':13,'l':14}
output-: {'a':10,'b':300,'c':50,'d':100,'e':600,'i':11,'j':12,'k':13,'l':14} '''

x = {'i':11,'j':12,'k':13,'l':14}
d.update(x)
print(d)


# //*-------Q6--------*//
'''  Q6.write a code to remove the key 'j' from dictionary d
output-: {'a':10,'b':300,'c':50,'d':100,'e':600,'i':11,'k':13,'l':14} '''

d.pop("j")
print(d)























