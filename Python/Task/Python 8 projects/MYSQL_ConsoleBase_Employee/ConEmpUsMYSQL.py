
import pymysql as p

# //*-- Connection to Database-----*//
def dbConnect():
    return p.connect(host="localhost", user="root", password="",database="pythonlect")


#//*-----Function to Show Employee Details-----*//

def readData():
    db = dbConnect()
    cr = db.cursor()

    sql = "select * from crudemp"
    cr.execute(sql)

    data = cr.fetchall()

    for d in data:
        print(f"{d[0]:^3} {d[1]:^10} {d[2]:^13} {d[3]:^30} {d[4]:^6} {d[5]:^5}\n")

    db.commit()
    db.close()



# //*-----Functon to insert Data-----*//

def insertDataEmp():

    eid = input("Enter Employee ID : ").lstrip()
    ename = input("Enter Employee Name : ").lstrip()
    econ = input("Enter Employee Contact : ").lstrip()
    eEmail = input("Enter Employee Email : ").lstrip()
    esal = input("Enter Employee Salary : ").lstrip()
    egen = input("Enter Employee Gender : ").lstrip().upper()


    t = (eid, ename, econ, eEmail, esal, egen)
    
    db = dbConnect()
    cr = db.cursor()

    sql = "insert into crudemp values(%s, %s, %s, %s, %s, %s)"
    cr.execute(sql,t)

    print("Data Inserted\n")
    db.commit()
    db.close()

# //*--- Function to Delete Employee Record----*//

def delEmp():
    eid = input("Enter Employee Id to Delete : ").lstrip()
    db = dbConnect()
    cr = db.cursor()

    sql = "delete from crudemp where id = %s;"
    cr.execute(sql,eid)
    print("Employee Detail Delete Sucessfully")
    db.commit()
    db.close()

    
# //*------------Function to show single Employee Data-----*//

def showEmpData():
    eid = input("Enter Employee ID : ").lstrip()
    db=dbConnect()
    cr=db.cursor()

    sql="select * from crudemp where id=%s"
    cr.execute(sql,eid)

    data = cr.fetchall()

    
    db.commit()
    db.close()
    
    for i in data:
        print(f"\nID :{i[0]:^2} \nName : {i[1]:^2} \nContact : {i[2]:^2} \nEmail : {i[3]:^2} \nSalary : {i[4]:^2} \nGender : {i[5]:^2}")
# //*----- Function to Update Employee Record----*//

def updateEmp(uep):
    db = dbConnect()
    cr = db.cursor()

    if uep == "1":
        eid = input("Enter Employee Id : ").lstrip()
        ename = input("Enter New Name : ").lstrip()
        t = (ename, eid)
        sql = "update crudemp set name=%s where id = %s;"
        cr.execute(sql,t)

    elif uep =="2":
        eid = input("Enter Employee Id : ").lstrip()
        econ = input("Enter New Contact : ").lstrip()
        t = (econ, eid)
        sql = "update crudemp set contact=%s where id = %s;"
        cr.execute(sql,t)

    elif uep =="3":
        eid = input("Enter Employee Id : ").lstrip()
        eEmail = input("Enter New Email : ").lstrip()
        t = (eEmail, eid)
        sql = "update crudemp set email=%s where id = %s;"
        cr.execute(sql,t)

    elif uep =="4":
        eid = input("Enter Employee Id : ").lstrip()
        eSal = input("Enter New Salary : ").lstrip()
        t = (eSal, eid)
        sql = "update crudemp set salary=%s where id = %s;"
        cr.execute(sql,t)

    elif uep =="5":
        eid = input("Enter Employee Id : ").lstrip()
        egen = input("Enter New Gender : ").lstrip()
        t = (egen, eid)
        sql = "update crudemp set gender=%s where id = %s;"
        cr.execute(sql,t)

    elif uep =="6":
        eid = input("Enter Employee Id : ").lstrip()
        eNeid = input("Enter New Employee Id : ").lstrip()
        t = (eNeid, eid)
        sql = "update crudemp set id=%s where id = %s;"
        cr.execute(sql,t)
        
    elif uep =="6":
        empLoop()
        
    db.commit()
    db.close()
    

# //*- Function to run Selection Loop----------------//

def empLoop():

    while True:

        print("\nEnter 1 to Show Emp Full Recird")
        print("Enter 2 to Add Employee")
        print("Enter 3 to Update Employee Details")
        print("Enter 4 to Delete Employee Record")
        print("Enter 5 to show Emplyee Data")
        print("Enter 6 to Exit\n")

        choi = input("Enter your Choice : ").lstrip()
        print("\n")

        if choi == "1":
            readData()

        elif choi =="2":
            insertDataEmp()

        elif choi =="3":
            
            print("\nEnter 1 to Update Employee Name")
            print("Enter 2 to Update Employee Contact")
            print("Enter 3 to Update Employee Email")
            print("Enter 4 to Update Employee Salary")
            print("Enter 5 to Update Employee Gender")
            print("Enter 6 to Update Employee ID")
            print("Enter 7 to Exit\n")

            uep = input("Enter Your Choice : ").lstrip()
            updateEmp(uep)

        elif choi =="4":
             delEmp()

        elif choi =="5":
            showEmpData()

        elif choi =="6":
            print("6")
        
empLoop()
