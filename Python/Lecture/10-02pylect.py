
# //*----List Operations----------*//

# //*----append() ------------*//

'''list1 = ["Red", "Green", "Blue"]
list1.append("Black")
# print(list1)

# //* -----Extend------**/
list2 = ["Car", "Cycle", "Boat"]

list1.extend(list2)
print(list1);


# //*--------Remove------*//
list1.remove("Car")
print(list1)

# //*--------pop()-------*//
list1.pop()
print(list1)
'''

# //*------index()--------*//
##
##list3 = [1,2,3,4,5,6]
##z = list3.index(4)
##print(z)

# //*---------reverse()--------*//

##list4 = [1,33,45,64,12,34]
##list4.reverse()
##print(list4)


### //*------sort()--------*//

##list5 = [1,43,65,76,87,22,65,77]
##list5.sort()
##print(list5)

#//*------- sort in reverse()----*//

##list5.sort(reverse=True)
##print(list5)

# //*----String Sorting-----*//

##list6 = ["C", "a", "B", "b","c", "A"]
##print(list6)
# //*  Bug in sorting
##list6.sort()
##print(list6)

# //* ---Solution--*//
##list6.sort(key=str.lower)
##print(list6)

#//-----Count()-----*//
##list7 = [1,2,4,1,2,6,3,6,1,8,1]
##z = list7.count(1)
##print(z)


# //*----List Manupulation-----*//

#//*--------Update()-----**/

# //* Single value delete by indexing
list8 = [1,2,3,4,5,6,7,8,9,0]
##print(list8)
##list8[4]="five"
##print(list8)
##

#//* Multiple vlaues delete by slicing

##list8[ : 3] = ["one", "two"]
##print(list8)

# //* Some experements

list8[3:7]="this"
print(list8)

list8[3:7]=["this"]
print(list8)

# //*------ del --------*//
##del list8[4]
##print(list8)


#//*----------------**---------------------------------*//

# //*-------Dictionary------**/

d = {"father":50, "Mother":34, "sister":23}
##x = d.keys()
##print(x)
##
##
##y = d.values()
##print(y)
##
##z = d.items()
##print(z)
##
##getval = d.get("Mother")
##print(getval)
##
##getval2 = d.get("uncle", "dost not exixt")
##print(getval2)
##
##d.setdefault("uncle",55)
##print(d)
##
##getval3 = d.get("uncle")
##print(getval3)


d1 = {"a":2, "b":33, "c":31}

d.update(d1)
print(d)

##d.update('father', 21)
##print(d)


d.pop("Mother")
print(d)

x = d["b"]
print(x)

d["a"]=40
print(d)

d["a"]=55
print(d)
