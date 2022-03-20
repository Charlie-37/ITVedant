

# //*-- WAP to show method overriding in python------*//

class parentFather():
    def intro(self):
        return "Hello I am Father class"

class child(parentFather):
    def intro(self):
        return "Hello I am child class"


obj1 = child()
#print(obj1.intro())

''' OUTPUT : Hello Iam child class
Since intro is already present in the child class so the parentsFather class's intro is 
overrided by the child class.Because the first Priority if geven to the self class

'''
# //*-----------------**---------------------**//
# to manupulate the overriding or strop overriding we can use Super() function



class parentFather2():
    def intro(self):
        return "Hello I am Father class"

class child2(parentFather2):
    def intro(self):
        print("hello I am Child Class")
        return print(super(child2, self).intro())
        

obj1 = child2()
obj1.intro()