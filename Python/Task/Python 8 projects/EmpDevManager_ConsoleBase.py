
import pymysql as p



def dbConnect():
    return p.connect(host="Localhost", user="root", password="", database="empdevman")
# //*--- Employee Manager Develpoer Class-----*//

# //*- Function to Create ROW for Employee Manager Developer in Database--*//

def crRow(rtype,table):
    efirst = input(f"Enter {rtype} First Name : ").strip().lower()
    elast = input(f"Enter {rtype} Last Name : ").strip().lower()
    esal = input(f"Enter {rtype} Salary : ").strip()
    esal = int(esal)
    print("\n")

    emp1 = Employees(efirst, elast, esal)
    x,y,z,w = emp1.pushData()
    print(x,y,z,w)

    # pushing to database

    db = dbConnect()
    cr = db.cursor()
    a = None
    t = (x,y,z,w,a)
    sql = f"insert into {table} values(%s,%s,%s,%s,%s)"

    cr.execute(sql,t)
    print("Added Sucessfull")
    db.commit()
    db.close()

    
# //*---Function to Pull Data from Employee and Manager to use from DB---*//
def pullData(tab,efirst,elast):
    db = dbConnect()
    cr = db.cursor()

    sql = f"select * from {tab} where first = %s"

    cr.execute(sql,efirst)

    data = cr.fetchall()

    db.commit()
    db.close()

    for i in data:
        if efirst == i[0] and elast == i[1]:
                return data
# //*---To show Data of Employee and Manager from DB----*//          
def showdata(tab,efirst,elast):
    db = dbConnect()
    cr = db.cursor()

    t = (efirst,elast)
    sql = f"select * from {tab} where first = %s and last = %s"

    cr.execute(sql,t)

    data = cr.fetchall()

    db.commit()
    db.close()

    for i in data:
        if efirst == i[0] and elast == i[1]:
                print("\n")
                print(f"First Name : {i[0]}".title())
                print(f"Last Name : {i[1]}".title())
                print(f"Salary : {i[2]}")
                print(f"Email : {i[3]}")
                return data

# //*-----To Show Developer Details from DB-----*///
# Create Sperate because of one extra Column(Pro Lang)

def devdet(efirst,elast):
    db = dbConnect()
    cr = db.cursor()

    t = (efirst,elast)
    sql = f"select * from dev where first = %s and last = %s"

    cr.execute(sql,t)

    data = cr.fetchall()

    db.commit()
    db.close()

    for i in data:
        if efirst == i[0] and elast == i[1]:
                print("\n")
                print(f"First Name : {i[0]}".title())
                print(f"Last Name : {i[1]}".title())
                print(f"Salary : {i[2]}")
                print(f"Email : {i[3]}")
                print(f"Pro Language : {i[4]}")


# //*---Function to Push the Incremented Salary to DB----*//

def pushIncr(tab,efirst,elast,incr):
    db = dbConnect()
    cr = db.cursor()
    t = (incr, efirst, elast)
    sql = f"update {tab} set salary = %s where first = %s and last = %s"
    cr.execute(sql,t)
    print("Incremented Sucessfull")
    db.commit()
    db.close()
    

# //*---------Classes to peform Class--------*//

class Employees():
    empcount = 0
    incamt = 1.10

    def __init__(self,first,last,salary): 
        self.first = first
        self.last = last
        self.salary = salary
        self.email = f"{self.first.lower()}.{self.last.lower()}@itvedant.com"
        Employees.empcount+=1
        
    def pushData(self):
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

    def pushData(self):
        return self.first, self.last, self.salary, self.email, self.prolang



class Manager(Employees):
    incamt = 1.50
    def __init__(self, first, last, salary, employees=None):
        super().__init__(first, last, salary)
        if(employees is None):
            self.employees = []
        else:
            self.employees = employees

    def addemp(self,tab, emp,mang):
##        if(emp not in self.employees):
##            self.employees.append(emp)
        db = dbConnect()
        cr = db.cursor()

        t = (mang[0][0],emp[0],emp[1])
        sql = f"update {tab} set manager= %s where first = %s and last = %s"

        cr.execute(sql,t)
        db.commit()
        db.close()

        

    def removeemp(self, emp, mang):
##        if(emp in self.employees):
##            self.employees.remove(emp)
        db = dbConnect()
        cr = db.cursor()

        t = (mang[0][0],emp[0],emp[1])
        sql = f"update {tab} set manager= Null where first = %s and last = %s"

        cr.execute(sql,t)
        db.commit()
        db.close()
    
    def printemp(self,mang):
##        for emp in self.employees:
##            #print(f"----> {emp[0]}{emp[1]}")
##            print(emp)

        db = dbConnect()
        cr = db.cursor()
        t = (mang[0][0],mang[0][0])
        sql = "select first,last from emp where manager = %s union select first,last from dev where manager = %s"

        cr.execute(sql,t)
        empdev = cr.fetchall()

        db.commit()
        db.close()
        print("\n")
        for i in empdev:
            fullname = " ".join(i).title()
            print(f"----> {fullname}")
       

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



    
# //*----Function to Give User Choices-----------*//

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
        print("Enter 12 to Delete Employee from Manager")
        print("Enter 13 to delet Developer from Manager")
        print("Enter 14 to Show Employees and Developer under Manager")
        print("\n")

        choi = input("Enter Your Choice : ").strip()
        print("\n")

        # Add Employee
        if choi == "1":    
            crRow("Employee","emp")

        # Add Developer   
        elif choi == "2":
            
            efirst = input(f"Enter Manger's First Name : ").strip().lower()
            elast = input(f"Enter Manger's Last Name : ").strip().lower()
            esal = input(f"Enter Manger's Salary : ").strip()
            esal = int(esal)
            elang  =  input(f"Enter Manger's Pro Language : ").strip().lower()
            print("\n")

            emp1 = Developer(efirst, elast, esal,elang)
            x,y,z,w,a = emp1.pushData()
            #print(emp1.pushData())
            #print(x,y,z,w,a)

            # pushing to database

            db = dbConnect()
            cr = db.cursor()
            b = None
            t = (x,y,z,w,a,b)
            sql = f"insert into dev values(%s,%s,%s,%s,%s,%s)"
            cr.execute(sql,t)

            print("Added Data Sucessfully")
            db.commit()
            db.close()

        # Add Manager 
        elif choi == "3":
           crRow("Manager","mang")

        # Show Emp Details
        elif choi == "4":
            efirst = input("Enter Employee First Name : ").strip().lower()
            elast = input("Enter Employee Last Name : ").strip().lower()
            showdata("emp",efirst,elast)

        # Show Developer Details
        elif choi == "5":
            
            efirst = input("Enter Developer First Name : ").strip().lower()
            elast = input("Enter Developer Last Name : ").strip().lower()
                            
            devdet(efirst,elast)
                

        # Show Manager Details
        elif choi == "6":
            efirst = input("Enter Manager First Name : ").strip().lower()
            elast = input("Enter Manager Last Name : ").strip().lower()
            showdata("mang",efirst,elast)

        # Increment Emp Salary
        elif choi == "7":
            efirst = input("Enter Employee First Name : ").strip().lower()
            elast = input("Enter Employee Last Name : ").strip().lower()
            data =pullData("emp",efirst,elast)

            if data != None:
                data =list(data)
                obj = Employees(data[0][0], data[0][1], data[0][2])
                incr = round(obj.increment(),2)

                pushIncr("emp",data[0][0],data[0][1],incr)
                showdata("emp",data[0][0],data[0][1])

                
        # Increment Dev Salary
        elif choi == "8":
            efirst = input("Enter Developer First Name : ").strip().lower()
            elast = input("Enter Developer Last Name : ").strip().lower()
            #data =pullData("dev",efirst,elast)
            db = dbConnect()
            cr = db.cursor()

            t = (efirst,elast)
            t = (efirst,elast)
            sql = "select * from dev where first = %s and last = %s"

            cr.execute(sql,t)

            data = cr.fetchall()

            if data != None:
                data =list(data)
                obj = Developer(data[0][0], data[0][1], data[0][2],data[0][4])
                incr = round(obj.increment(),2)

                pushIncr("dev",data[0][0],data[0][1],incr)
                #showdata("dev",data[0][0],data[0][1])
                devdet(data[0][0],data[0][1])

        # Increment Manager Salary
        elif choi == "9":
            efirst = input("Enter Manager First Name : ").strip().lower()
            elast = input("Enter Manager Last Name : ").strip().lower()
            data =pullData("mang",efirst,elast)

            if data != None:
                data =list(data)
                obj = Manager(data[0][0], data[0][1], data[0][2])
                incr = round(obj.increment(),2)

                pushIncr("mang",data[0][0],data[0][1],incr)
                showdata("mang",data[0][0],data[0][1])

        # Add Employee in Manager
        elif choi == "10":
            mfirst = input("Enter Manager First Name : ").strip().lower()
            mlast = input("Enter Manager Last Name : ").strip().lower()
            mdata = pullData("mang",mfirst,mlast)

            if mdata != None:
                efirst = input("Enter Employee First Name : ").strip().lower()
                elast = input("Enter Employee Last Name : ").strip().lower()
                edata = pullData("emp",efirst,elast)

                if edata != None:

                    for i in edata:
                        edatalist = list(i)
                        obj1 = Manager(mdata[0][0],mdata[0][1],mdata[0][2],edatalist)
                        obj1.addemp("emp",edatalist,mdata)

        # ADD developer in Manager
        elif choi == "11":
            mfirst = input("Enter Manager First Name : ").strip().lower()
            mlast = input("Enter Manager Last Name : ").strip().lower()
            mdata = pullData("mang",mfirst,mlast)

            if mdata != None:
                dfirst = input("Enter Developer First Name : ").strip().lower()
                dlast = input("Enter Developer Last Name : ").strip().lower()
                ddata = pullData("dev",dfirst,dlast)

                if ddata != None:

                    for i in ddata:
                        ddatalist = list(i)
                        obj1 = Manager(mdata[0][0],mdata[0][1],mdata[0][2],ddatalist)
                        obj1.addemp("dev",ddatalist,mdata)

        #Delete Employee from Manager
        elif choi == "12":
            mfirst = input("Enter Manager First Name : ").strip().lower()
            mlast = input("Enter Manager Last Name : ").strip().lower()
            mdata = pullData("mang",mfirst,mlast)

            if mdata != None:
                efirst = input("Enter Employee First Name : ").strip().lower()
                elast = input("Enter Employee Last Name : ").strip().lower()
                edata = pullData("emp",efirst,elast)

                if edata != None:

                    for i in edata:
                        edatalist = list(i)
                        obj1 = Manager(mdata[0][0],mdata[0][1],mdata[0][2],edatalist)
                        obj1.removeemp(self, emp, mang)

        #Delete Developer from Manager
        elif choi == "13":
            mfirst = input("Enter Manager First Name : ").strip().lower()
            mlast = input("Enter Manager Last Name : ").strip().lower()
            mdata = pullData("mang",mfirst,mlast)

            if mdata != None:
                dfirst = input("Enter Developer First Name : ").strip().lower()
                dlast = input("Enter Developer Last Name : ").strip().lower()
                ddata = pullData("dev",dfirst,dlast)

                if ddata != None:

                    for i in ddata:
                        ddatalist = list(i)
                        obj1 = Manager(mdata[0][0],mdata[0][1],mdata[0][2],ddatalist)
                        obj1.removeemp("dev", ddatalist, mang)

        # show all EMP and DEV in Mnager
        elif choi == "14":
            mfirst = input("Enter Manager First Name : ").strip().lower()
            mlast = input("Enter Manager Last Name : ").strip().lower()
            mdata = pullData("mang",mfirst,mlast)

            if mdata != None:
                obj1 = Manager(mdata[0][0],mdata[0][1],mdata[0][2])
                obj1.printemp(mdata)
                

            
            
        
        
empdev()    















        
