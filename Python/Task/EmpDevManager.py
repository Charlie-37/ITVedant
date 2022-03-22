

# //*--- Employee Manager Develpoer Class-----*//

class Employees():
    empcount = 0
    incamt = 1.10

    def __init__(self,first,last,salary): 
        self.first = first
        self.last = last
        self.salary = salary
        self.email = f"{self.first.lower()}.{self.last.lower()}@itvedant.com"
        Employees.empcount+=1

    def increment(self):
        self.salary = self.salary * self.incamt
        return self.salary

    def fullname(self):
        return f"{self.first.title()} {self.last.title()}"


class Developer(Employees):
    incamt = 1.30
    def __init__(self, first, last, salary, prolang):
        super().__init__(first, last, salary)
        self.prolang = prolang



class Manager(Employees):
    def __init__(self, first, last, salary, employees=None):
        super().__init__(first, last, salary)
        if(employees is None):
            self.employees = []
        else:
            self.employees = employees

    def addemp(self, emp):
        if(emp not in self.employees):
            self.employees.append(emp)

    def removeemp(self, emp):
        if(emp in self.employees):
            self.employees.remove(emp)
    
    def printemp(self):
        for emp in self.employees:
            print(f"----> {emp.fullname()}")
       

emp1 = Employees("sunil", "bhave", 25000)
emp2 = Employees("bhavesh", "ainkar", 2200)
emp3 = Employees("Rutuja", "sawant", 10000)
emp4 = Employees("Mahesh", "bhat", 15000)
emp5 = Employees("suraj", "surwanshi", 45000)
emp6 = Employees("Tejas", "Jadhav", 75000)

print(emp6.increment())

dev1 = Developer("Dipali", "Bhangrath", 300000,"Python")
dev2 = Developer("Ruchita", "Gurav", 400000,"Java")

print(dev2.fullname())
print(dev2.email)
print(dev2.increment())



manag1 = Manager("Sapnil", "rajesh", 45222)
manag2 = Manager("Rahul", "kanojiya", 65222)

manag2.addemp(emp2)
manag2.addemp(emp1)
manag2.addemp(emp5) 
manag2.addemp(dev2) 

print(manag2.printemp())

manag2.removeemp(emp5)
print(manag2.printemp())
print(manag2.fullname())
print(manag2.increment())

