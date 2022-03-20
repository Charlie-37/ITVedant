
# //*---------WAP to show various inheritance in python----*//

# //*--------- 1. Single Inheritance------------*//

from ast import Pass
from turtle import color


class parent1():
    def intro(self):
        return "Hello I am Parent Class"


class child1(parent1):
    pass 

obj1 = child1()
print(obj1.intro())

#Output: Hello I am Parent Class

# //*---------------------****----------------------//

# //*--------- 2. Multiple Inheritance------------*//

class Father1():
    eyes = "Black"
    height = "Tall"

class Mom1():
    eyes = "Blue"
    face = "Oval"


class child2(Mom1,Father1):
    pass

obj2 = child2()
print(obj2.eyes)   # Output will be blue Coz Mom1 class is first Argument and no eyes in child2 class
print(obj2.height)
print(obj2.face)

'''OUTPUT
Blue
Tall
Oval

'''

# //*---------------------****----------------------//

# //*--------- 3. Multilevel Inheritance------------*//

class Parent2():
    height = "Tall"
    eyes = "Green"

class Child3(Parent2):
    height = "Short"
    face = "Square"


class GrandChild1(Child3):
    pass

obj3 = GrandChild1()
print(obj3.eyes)  
print(obj3.height)
print(obj3.face)

'''OUTPUT
Green 
Short 
Square

'''


# //*---------------------****----------------------//

# //*--------- 4. Hierarchical Inheritance------------*//

class Parent3():
    height = "Tall"
    eyes = "Green"
    face = "Oval"
    color = "Light"

class Child4(Parent3):
    pass

class Child5(Parent3):
    pass

class Child6(Parent3):
    pass

obj4 = Child4()
obj5 = Child5()
obj6 = Child6()
print(obj4.face)  
print(obj5.eyes)
print(obj6.color)

'''OUTPUT
Oval  
Green 
Light 

'''

# //*---------------------****----------------------//

# //*--------- 5. Hybrid Inheritance------------*//

class GrandFather2():
    height = "Tall"
    eyes = "Black"
    FootSize = 10

class Father2(GrandFather2):
    height = "Medium"
    eyes = "Green"
    color = "Dark"

class Mom2(GrandFather2):
    color="light"
    face = "Oval"

class Child7(Mom2, Father2):
    pass

obj7 = Child7()

print(obj7.face)  
print(obj7.eyes)
print(obj7.color)
print(obj7.FootSize)

'''OUTPUT
Oval
Green
light
10
'''