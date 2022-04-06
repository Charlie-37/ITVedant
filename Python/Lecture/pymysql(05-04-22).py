import pymysql as p



# //*--Function to Db Connectivity----*//
def dbConnect():

    return p.connect(host="localhost", user="root",password="",database="pythonlect")
    


# //*--- Function to insertion Data---*//
def insertData(t):
    db = dbConnect()
    cr = db.cursor()

    sql = "insert into itvtable values (%s, %s, %s, %s)"

    cr.execute(sql, t)
    print("Data inserted")
    db.commit()
    db.close()


# //*- Function to Get user Details----*//
def getData():
    ids = int(input("Enter Id : "))
    name = input("Enter Name : ")
    email = input("Enter Email : ")
    add = input("Enter Address : ")

    t = (ids,name,email,add)

    insertData(t)


#getData()

# //*--- Function To Update Db data-----*//
def updateData(t):
    db= dbConnect()
    cr = db.cursor()

    sql = "update itvtable set name=%s, email=%s, address=%s where id=%s"
    cr.execute(sql,t)

    print("Data Updated Sucessfully")

    db.commit()
    db.close()

# //* Funtion to Fetch DB data---*//

def read():
    db= dbConnect()
    cr = db.cursor()

    sql = "select * from itvtable"
    cr.execute(sql)

    data = cr.fetchall()

    for d in data:
        print(f"{d[0]:^3} {d[1]:^20} {d[2]:^20} {d[3]:^15}")

    db.commit()
    db.close()

#read()


def login():
    db= dbConnect()
    cr = db.cursor()

    sql = "select email, address from itvtable"
    cr.execute(sql)

    data = cr.fetchall()

    db.commit()
    db.close()

    return data


def loginVal():
    
    u = "teja@itv.com"
    p = "Mulund"
    data = login()

    if (u,p) in data:
        return print("Access Granted")

    else:
        return print("Denied")

loginVal()
