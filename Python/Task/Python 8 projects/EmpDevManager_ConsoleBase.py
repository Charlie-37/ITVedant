
import pymysql as p

def dbConnect():
    return p.connect(host="Localhost", user="root", password="", database="empdevman")
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

    def pushDet(self):
        return self.first, self.last, self.salary, self.email 

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
       

##emp1 = Employees("sunil", "bhave", 25000)
##emp2 = Employees("bhavesh", "ainkar", 2200)
##emp3 = Employees("Rutuja", "sawant", 10000)
##emp4 = Employees("Mahesh", "bhat", 15000)
##emp5 = Employees("suraj", "surwanshi", 45000)
##emp6 = Employees("Tejas", "Jadhav", 75000)
##
##print(emp6.increment())
##
##dev1 = Developer("Dipali", "Bhangrath", 300000,"Python")
##dev2 = Developer("Ruchita", "Gurav", 400000,"Java")
##
##print(dev2.fullname())
##print(dev2.email)
##print(dev2.increment())
##
##
##
##manag1 = Manager("Sapnil", "rajesh", 45222)
##manag2 = Manager("Rahul", "kanojiya", 65222)
##
##manag2.addemp(emp2)
##manag2.addemp(emp1)
##manag2.addemp(emp5) 
##manag2.addemp(dev2) 
##
##print(manag2.printemp())
##
##manag2.removeemp(emp5)
##print(manag2.printemp())
##print(manag2.fullname())
##print(manag2.increment())


def empdev():
    while True:
        print("\n")
        print("Enter 1 to Add Employee")
        print("Enter 2 to Add Developer")
        print("Enter 3 to Add Manager")
        print("Enter 4 to Show Employee Details")
        print("Enter 5 to Show Developer Details")
        print("Enter 6 to Show Manager Details")
        print("Enter 7 to Show Increment Employee Salary")
        print("Enter 8 to Show Increment Developer Salary")
        print("Enter 9 to Show Increment Manager Salary")
        print("Enter 10 to Add Employee in Manager")
        print("Enter 11 to Add Developer in Manager")
        print("\n")

        choi = input("Enter Your Choice : ").strip()
        print("\n")

        if choi == "1":
            efirst = input("Enter Employee First Name : ").strip()
            elast = input("Enter Employee Last Name : ").strip()
            esal = input("Enter Employee Salary : ").strip()
            esal = int(esal)

            emp1 = Employees(efirst, elast, esal)
            x,y,z,w = emp1.pushDet()
            print(x,y,z,w)

            # pushing to database

            db = dbConnect()
            cr = db.cursor()

            t = (x,y,z,w)
            sql = "insert into emp values(%s,%s,%s,%s)"

            cr.execute(sql,t)

            db.commit()
            db.close()

            
            

        elif choi == "2":
            pass

        elif choi == "3":
            pass

        elif choi == "4":
            pass

        elif choi == "5":
            pass

        elif choi == "6":
            pass

        elif choi == "7":
            pass

        elif choi == "8":
            pass

        elif choi == "9":
            pass

        elif choi == "10":
            pass

        elif choi == "11":
            pass
        
        
empdev()    















        
