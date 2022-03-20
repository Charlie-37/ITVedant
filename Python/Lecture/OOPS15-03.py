
# //*--------Class Inheritance-------------*//





# //*--------Single Level Inheritence-------*//
# class parent():
    
#     voice = "rough"
#     hair = "balck"
#     eyes = "brown"

#     def intro(self):
#         return "Hello am Parent"


# class child(parent):
#     def intro(self):
#         return "Hello am Child"

# obj1 = child()

# print(obj1.intro())
# print(obj1.voice)
# print(obj1.eyes)


# //*--------double Level Inheritence-------*//

# class dad():
#     voice = "Rough"
#     eyes = "brown"
#     skin ="dark"

#     def intro(self):
#         return "Hello I Am Dad class"


# class mom():
    
#     eyes = "Blue"
#     height ="tall"
#     face = "Round"

#     def intro(self):
#         return "Hello I Am Mom class"

# class child(mom,dad):
#     def intro(self):
#         return "Hello I Am Child Class"


# obj2 = child()

# print(obj2.voice)
# print(obj2.eyes)
# print(obj2.intro())


# //*--------Herarchichal Level Inheritence-------*//

# class grandFather():
#     hair = "white"
#     height = "short"
#     eyes = "grey"
#     voice = "Heigh Pitch"

#     def intro(self):
#         return "Hello I am GrandFather Class "

# class dad(grandFather):
#     voice = "Rough"
#     eyes = "brown"
#     skin ="dark"

#     def intro(self):
#         return "Hello I Am Dad class"


# class mom(grandFather):
    
#     eyes = "Blue"
#     height ="tall"
#     face = "Round"

#     def intro(self):
#         return "Hello I Am Mom class"

# class child(mom,dad):
#     def intro(self):
#         return "Hello I Am Child Class"


# obj2 = child()

# print(obj2.voice)
# print(obj2.eyes)
# print(obj2.hair)
# print(obj2.intro())


# //*--------Super() Inheritence-------*//

class emp():
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
        self.email = f"{self.name.lower()}{self.age}@Itvedant.com"

    def intro(self):
        print(self.name)
        print(self.age)
        print(self.salary)
        print(self.email)


class developer(emp):
    def __init__(self,name,age,salary,prolang):
        super().__init__(name,age,salary)
        self.prolang = prolang

    def intro(self):
        super().intro()
        print(self.prolang)
        # return "Hello World"

obj3 = developer("Sunil",23,45000,"Python")

obj3.intro()