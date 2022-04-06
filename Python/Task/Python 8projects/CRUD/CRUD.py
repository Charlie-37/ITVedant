
##record= [
##    
##    (1,"Sunil",10,"Thane",2000),
##    (2,"Bhavesh",23,"Karjat",300),
##    (3,"Tejas",25,"Mulund",400),
##    (4,"Prasad",22,"Nashik",500),
##    (5,"Sandeep",24,"Badlapur",500)
##    ]
##
def addRec(Eid,Fname,Lname,Sal,Econtact):
    f = open("record.txt","a")

    print(f"{Eid:^3} {Fname:^8} {Lname:^8} {Sal:^7} {Econtact:^14}\n")
    f.write(f"{Eid:^3} {Fname:^8} {Lname:^8} {Sal:^7} {Econtact:^14}\n")
    f.close()



def readRec():
    f = open("record.txt","r")
    record = f.read()
##    for Eid,Fname,Lname,Sal,Econtact in record:
##        print(f"{Eid:^3} {Fname:^8} {Lname:^8} {Sal:^7} {Econtact:^14}\n")
    print(record)
    



def getRow(eID):
    f = open("record.txt","r")
    record = f.readlines()
    #print(record[1])
    for i in range(len(record)):
        #print(record[i])
        listR = record[i].split()
        EmpId = listR[0]
        #EmpId = int(EmpId)
        
    if eID == EmpId:
        print(f"ID: {listR[0]} \nFName : {listR[1]} \nLname : {listR[2]} \nSalary : {listR[3]}  \nContact : {listR[4]} ","\n")
    else:
        print("ID does Not Exist\n")

       
       
    f.close()


def UpEmp(empId):
    f = open("record.txt","r")
    record = f.readlines()
    #print(record[1])
    for i in range(len(record)):
        #print(record[i])
        listR = record[i].split()
        EmpId = listR[0]
        EmpId = int(EmpId)
        
        if empId == EmpId:
            
            Eid = input("Enter Employee ID : ").lstrip()
            #Eid = Eid.lstrip()
            Eid = int(Eid)

            Fname = input("Enter Employee First Name : ").lstrip()
            Lname = input("Enter Employee Last Name : ").lstrip()
            Salary = input("Enter Employee Salary : ").lstrip()
            Sal = int(Salary)
            Econtact = input("Enter Employee Contact: " ).lstrip()
            
            addRec(Eid,Fname,Lname,Sal,Econtact)
        else:
            print("ID does Not Exist\n")
    pass











##
##readRec(record)
##
##def UpdateRec():
##    f = open("record.txt","a")
##    for i,n,a,p,s in record:
##        f.write(f"{i:^3} {n:^8} {a:^3} {p:^10} {s:^4}\n")
##    f.close()




# //*  Creating While Loop


def MainEmp():
    while True:
        print("Employee Details\n")
        print("Enter 1 for Add Employee")
        print("Enter 2 for Veiw Employee")
        print("Enter 3 for View Full Employee List")
        print("Enter 4 for Update Employee")
        print("Enter 5 for Delete Employee")
        print("Enter 6 for Exit\n")

        choi  = input("Enter Your Choice : ")
        choi = choi.lstrip()

        if choi == "1":
            Eid = input("Enter Employee ID : ").lstrip()
            #Eid = Eid.lstrip()
            Eid = int(Eid)

            Fname = input("Enter Employee First Name : ").lstrip()
            Lname = input("Enter Employee Last Name : ").lstrip()
            Salary = input("Enter Employee Salary : ").lstrip()
            Sal = int(Salary)
            Econtact = input("Enter Employee Contact: " ).lstrip()

            addRec(Eid,Fname,Lname,Sal,Econtact)

            
            
            
            #addRec()
        elif choi == "2":
            eID = input("Enter Eid to get Details : ").lstrip()
            #eID = int(eID)
            getRow(eID)



            
        elif choi == "3":
            readRec()
        elif choi == "4":
            empId = input("Enter Emp ID to update : ").lstrip()
            empId = int(empId)
            UpEmp(empId)
            
        elif choi == "5":
            print("5")
        elif choi == "6":
            exi = ("Are You Sure Y/N : ")
            exi = exi.lower().lstrip()
        

        
    

MainEmp()






























