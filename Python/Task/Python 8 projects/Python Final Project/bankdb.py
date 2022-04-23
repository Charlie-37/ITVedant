
import pymysql as p
import datetime
import random as rd

def dbConnect():
    return p.connect(host="localhost", user="root",password="",database="atmbank")



# //*----User Login------*//
def user_login():
    db = dbConnect()
    cr = db.cursor()
    sql = "select * from user ;"

    cr.execute(sql)
    data = cr.fetchall()
    db.commit()
    db.close()

    passid = []
    for i in data:
        t=(i[2],i[3])
        passid.append(t)
    return passid


# //*----Staff Login------*//
def staff_login():
    db = dbConnect()
    cr = db.cursor()
    sql = "select * from staff ;"

    cr.execute(sql)
    data = cr.fetchall()
    db.commit()
    db.close()

    passid = []
    for i in data:
        t=(i[2],i[3])
        passid.append(t)

    return passid
#//*-----------select User Details-------------*//
def selectuser(t):
        db = dbConnect()
        cr = db.cursor()
        sql = "select fname,lname,usname,password,contact,aadhar,city,DATE(dob),acctype,gender,balance,accno,cvv,pin from user where usname=%s and password = %s"
        cr.execute(sql,t)
        data = cr.fetchall()
        db.commit()
        db.close()

        return data[0]

def date():
        db = dbConnect()
        cr = db.cursor()
        sql = "select DATE(dob) from user"
        cr.execute(sql)
        data = cr.fetchall()
        db.commit()
        db.close()

        return print(data)
# //*--------deposite user Money ***/

def deposite_money(accoun,passw,amt):

    db = dbConnect()
    cr = db.cursor()
    t = (accoun,passw)
    sql = "select * from user where accno=%s and password=%s"
    cr.execute(sql,t)
    data = cr.fetchall()
    db.commit()
    db.close()

    if data!=None:
        amt = int(amt)
        bal = list(data[0])
        # print(list(data))
        bal[10] += amt

        db = dbConnect()
        cr = db.cursor()
        t = (bal[10],accoun,passw)
        sql = "update user set balance=%s where accno=%s and password=%s"
        cr.execute(sql,t)
        db.commit()
        db.close()

        return True
    else:
        return False


#//*-----Transfer User Money to other account
def transferMoney(user_accoun,passw,amount,payee_accoun):
        db = dbConnect()
        cr = db.cursor()
        t = (user_accoun,passw)
        sql = "select * from user where accno=%s and password=%s "
        cr.execute(sql,t)
        user_data = cr.fetchall()
        db.commit()
        db.close()
        user_bal = user_data[0][10]
        user_bal = int(user_bal)


        db = dbConnect()
        cr = db.cursor()
        sql = "select * from user where accno=%s "
        cr.execute(sql,payee_accoun)
        payee_data = cr.fetchall()
        db.commit()
        db.close()
        payee_bal = payee_data[0][10]
        payee_bal = int(payee_bal)

        amount = int(amount)


        if user_data != None:
            if payee_data !=None:
                if amount<=user_bal:
                    user_bal = user_bal-amount
                    payee_bal = payee_bal+amount

                    # //*---Updating Balances----*//
                    db = dbConnect()
                    cr = db.cursor()
                    t = (user_bal,user_accoun)
                    sql = "update user set balance=%s where accno=%s "
                    cr.execute(sql,t)
                    db.commit()
                    db.close()

                    db = dbConnect()
                    cr = db.cursor()
                    t = (payee_bal,payee_accoun)
                    sql = "update user set balance=%s where accno=%s "
                    cr.execute(sql,t)
                    db.commit()
                    db.close()


                else:
                    return "Low Account Balance"
            else:
                return "Account does not Exist"
            
        else:
            return "Account does not Exist"


# //*----Edit Staff Details------*//



# //*------------------Class of User----------------------------*//
class userdet():
    def __init__(self,fname, lname, usname, passw, contact, adhar, city, dob, acctype, gender):
        self.fname = fname
        self.lname = lname
        self.usname = usname
        self.passw = passw
        self.contact = contact 
        self.adhar = adhar
        self.city = city
        self.dob = dob
        self.acctype = acctype
        self.gender = gender
        

        
    def cruser(self):
        self.balance = 0

        self.accno = 0
        for i in range(0,5):
            self.accno = (self.accno*10) +rd.randint(0,9)

        self.pin = None
        self.cvv = 0
        for i in range(0,3):
            self.cvv = (self.cvv*10) +rd.randint(0,9)
        db = dbConnect()
        cr = db.cursor()
        sql = " insert into user values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s); "
        t = (self.fname,self.lname,self.usname,self.passw,self.contact,self.adhar,self.city,self.dob,self.acctype,self.gender,self.balance,self.accno,self.cvv,self.pin)

        cr.execute(sql,t)
        db.commit()
        db.close()
        return print("Insertion Sucessful")


    def showuser(self):
        db = dbConnect()
        cr = db.cursor()
        t = (self.usname,self.passw)
        sql = "select * from user where usname=%s and password = %s"
        cr.execute(sql,t)
        data = cr.fetchall()
        db.commit()
        db.close()

        return data[0]

    def updateUser(self,accoun):
        db = dbConnect()
        cr = db.cursor()
        sql = "update user set fname=%s ,lname=%s ,usname=%s ,password=%s ,contact=%s ,aadhar=%s ,city=%s ,dob=%s ,acctype=%s,gender=%s where accno=%s"
        t = (self.fname,self.lname,self.usname,self.passw,self.contact,self.adhar,self.city,self.dob,self.acctype,self.gender,accoun)
        # t = (fname,lname,usname,passw,contact,adhar,city,dob,acctype,gender,accoun)
        cr.execute(sql,t)
        db.commit()
        db.close()

      # //*----------End OF USER CLASS----------------*///

#//*---------------------------Staff Class---------------------*//
class staffdet():
    def __init__(self,fname, lname, usname, passw, contact, adhar, city, dob, pos, gender):
        self.fname = fname
        self.lname = lname
        self.usname = usname
        self.passw = passw
        self.contact = contact 
        self.adhar = adhar
        self.city = city
        self.dob = dob
        self.pos = pos
        self.gender = gender


        
    def crstaff(self):
        db = dbConnect()
        cr = db.cursor()
        sql = "insert into staff values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s); "
        t = (self.fname,self.lname,self.usname,self.passw,self.contact,self.adhar,self.city,self.dob,self.pos,self.gender)

        cr.execute(sql,t)
        db.commit()
        db.close()
        return print("Insertion Sucessful")

   # //*----------End OF STAFF CLASS----------------*///


#//*-----------select User Details-------------*//
def selectstaff(t):
        db = dbConnect()
        cr = db.cursor()
        sql = "select fname,lname,usname,password,contact,aadhar,city,DATE(dob),position,gender from staff where usname=%s and password = %s"
        cr.execute(sql,t)
        data = cr.fetchall()
        db.commit()
        db.close()

        return data[0]

#//*----------All User List Details-------------*//

def selectAllUser():
    db = dbConnect()
    cr = db.cursor()
    sql ="select fname,lname,usname,password,contact,aadhar,city,DATE(dob),acctype,gender,balance,accno,cvv,pin from user"
    cr.execute(sql)
    data = cr.fetchall()
    db.commit()
    db.close()

    return data

#//*-----------select User Details TO Update By Staff-------------*//
def selectuser_staff(t):
        db = dbConnect()
        cr = db.cursor()
        sql = "select fname,lname,usname,password,contact,aadhar,city,DATE(dob),acctype,gender,balance,accno,cvv,pin from user where accno=%s"
        cr.execute(sql,t)
        data = cr.fetchall()
        db.commit()
        db.close()

        return data[0]


#//*-----------delete User Details By Staff-------------*//
def deleteuser_staff(accnum):
        db = dbConnect()
        cr = db.cursor()
        sql = "delete from user where accno=%s"
        cr.execute(sql,accnum)
        db.commit()
        db.close()




#//*---------------------------ATM METHODS-------------*//
#//*---------------------ACCcheck-------------*//

def Atmaccdet(accoun,accCvv):
        db = dbConnect()
        cr = db.cursor()
        t = (accoun,accCvv)
        sql = "select fname,lname,usname,password,contact,aadhar,city,DATE(dob),acctype,gender,balance,accno,cvv,pin from user where accno=%s and cvv = %s"
        cr.execute(sql,t)
        data = cr.fetchall()
        db.commit()
        db.close()
        return data[0]

    
