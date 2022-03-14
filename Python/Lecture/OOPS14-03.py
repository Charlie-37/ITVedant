
# //*-----OOPS--------*//

# class human():
#     eyes = "black"
#     hair = "Brown"

#     def speak(self):
#         return "I am Speaking "

#     def walk(self):
#         return "I am walking"


# obj = human()

# print(obj.eyes)
# print(obj.hair)
# print(obj.speak())
# print(obj.walk())


# //*-----------OOPS self value pass importance of self---*//

name ="Sunil"
age = 23

class myClass:
    name = "Bhavesh"
    age = 22

    def intro(self):
        return f"Hello my name is {self.name}, My age is {self.age}"

    def intro2(self):
        return f"Hello my name is {name}, My age is {age}"


objp = myClass()
print(objp.intro())
print(objp.intro2()) 
