


#//*------------Function To Show Record----------*//

def ShowRec():
    f = open("instiRec.txt","r")
    record = f.readlines()
    f.close

    for d in record:
        print(d)

#//*------------Function To Sort the Record----------*//

def sortRec():
    f = open("instiRec.txt","r")
    record = f.readlines()
    f.close
    rec = []
    for d in record:
        x = d.strip().split()
        rec.append(x)
        
    # lambda function to sort a list inside list 
    rec.sort(key = lambda x : x[0])

    f = open("instiRec.txt","w")

    for i,j,k,l in rec:
         f.write(f"{i:^3} {j:^15} {k:^12} {l:^7}\n")
    f.close()

    
# //*----Function to Add Record--------*//

def addRecord(eid, ename, ecourse, esalary):
    f = open("instiRec.txt","a")

    print("\n")
    #print(f"{eid:^3} {ename:^15} {ecourse:^12} {esalary:^7}\n")
    f.write(f"{eid:^3} {ename:^15} {ecourse:^12} {esalary:^7}\n")

    #print("Record Added Sucessfully")
    f.close()
    sortRec()
    
#//*------------Function To Show Employee Course----------*//
def showCourse(eid):

    f = open("instiRec.txt","r")
    record = f.readlines()

    f.close()

    #print(record)

    for i in range(len(record)):
        #print(record[i])
        listR = record[i].split()
        #print(listR)

        empId = listR[0]

        if eid == empId:
            print("\n")
            print("Course : ",listR[2])



#//*------------Function To Update Employee Course----------*//

def upEmpCourse(eid):
    f = open("instiRec.txt","r")
    record = f.readlines()

    f.close()

    newData=[]

    for d in record:
        x = d.strip().split()
        newData.append(x)

    #print(newData)
    eid = int(eid)

    necou = input("Enter New Course : ").strip()
    
    ueid = newData[eid-1][0]
    uename = newData[eid-1][1]
    uecourse = necou
    uesalary = newData[eid-1][3]

    newData.pop(eid-1)
    #print(newData[eid-1][0])

    f = open("instiRec.txt","w")

    for i,j,k,l in newData:
         f.write(f"{i:^3} {j:^15} {k:^12} {l:^7}\n")
    f.close()

    
    addRecord(ueid, uename, uecourse, uesalary)
    sortRec()
    

    
#//*------------Function To Delete Employee Course----------*//

def delEmpCourse(eid):
    f = open("instiRec.txt","r")
    record = f.readlines()

    f.close()

    newData=[]

    for d in record:
        x = d.strip().split()
        newData.append(x)

    #print(newData)
    eid = int(eid)

    
    ueid = newData[eid-1][0]
    uename = newData[eid-1][1]
    uecourse = "Null"
    uesalary = newData[eid-1][3]

    newData.pop(eid-1)
    #print(newData[eid-1][0])

    f = open("instiRec.txt","w")

    for i,j,k,l in newData:
         f.write(f"{i:^3} {j:^15} {k:^12} {l:^7}\n")
    f.close()

    
    addRecord(ueid, uename, uecourse, uesalary)
    sortRec()

#//*------------Function To Update Employee Details----------*//

def upEmpdetails(eid):
    f = open("instiRec.txt","r")
    record = f.readlines()

    f.close()

    newData=[]

    for d in record:
        x = d.strip().split()
        newData.append(x)

    #print(newData)
    eid = int(eid)
    
    print("\n")
    print("Enter 1 to Update Employee ID")
    print("Enter 2 to Update Employee Name")
    print("Enter 3 to Update Employee Course")
    print("Enter 4 to Update Employee Salary")
    print("Enter 5 to Exit")
    print("\n")

    uchoi = input("Enter Your Choice : ").strip()

    if uchoi == "1":
        ueid = input("Enter New Employee ID : ").strip()
        uename = newData[eid-1][1]
        uecourse = newData[eid-1][2]
        uesalary = newData[eid-1][3]
    
    elif uchoi == "2":
        ueid = newData[eid-1][0]
        uename = input("Enter New Employee Name : ").strip()
        uecourse = newData[eid-1][2]
        uesalary = newData[eid-1][3]

    elif uchoi == "3":
        ueid = newData[eid-1][0]
        uename = newData[eid-1][1]
        uecourse = input("Enter New Employee Course : ").strip()
        uesalary = newData[eid-1][3]

    elif uchoi == "4":
        ueid = newData[eid-1][0]
        uename = newData[eid-1][1]
        uecourse = newData[eid-1][2]
        uesalary = input("Enter New Employee Salary : ").strip()
    
    elif uchoi == "5":
        userChoi()
    

    newData.pop(eid-1)
    #print(newData[eid-1][0])

    f = open("instiRec.txt","w")

    for i,j,k,l in newData:
         f.write(f"{i:^3} {j:^15} {k:^12} {l:^7}\n")
    f.close()

    
    addRecord(ueid, uename, uecourse, uesalary)
    sortRec()
# //*----Console to Give Choices-------------*///

def userChoi():

    print("\n")
    print("Enter 1 to Add Record")
    print("Enter 2 to Show Course")
    print("Enter 3 to Update Course")
    print("Enter 4 to Update Employee Detail")
    print("Enter 5 to Delete Course")
    print("\n")

    choi = input("Enter Your Choice : ").lstrip()
    print("\n")

    if choi == "1":
        eid = input("Enter Employee ID : ").lstrip()
        ename = input("Enter Employee Name : ").lstrip()
        ecourse = input("Enter Employee Course : ").lstrip()
        esalary = input("Enter Employee Salary : ").lstrip()

        addRecord(eid, ename, ecourse, esalary)
        ShowRec()
        userChoi()
    

    elif choi == "2":
        eid = input("Enter Employee ID : ").lstrip()
        showCourse(eid)
        userChoi()

    elif choi == "3":
        eid = input("Enter Employee ID : ").lstrip()
        upEmpCourse(eid)
        ShowRec()
        userChoi()

    elif choi == "4":
        eid = input("Enter Employee ID : ").lstrip()
        upEmpdetails(eid)
        ShowRec()
        userChoi()

    elif choi == "5":
        eid = input("Enter Employee ID : ").lstrip()
        delEmpCourse(eid)
        ShowRec()
        userChoi()

    else:
        print("Invalid Choice")


userChoi()

