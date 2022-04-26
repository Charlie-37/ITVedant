
import pymysql as p
from datetime import datetime
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
        # sql = "select * from user where usname=%s and password = %s"
        sql = "select fname,lname,usname,password,contact,aadhar,city, dob ,acctype,gender,balance,accno,cvv,pin from user where usname=%s and password = %s"
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

# //*---------------PIN CHANGE-------------------*//

def OldPinCheck(user_accoun):
        db = dbConnect()
        cr = db.cursor()
        sql = "select pin from user where accno=%s ;"
        cr.execute(sql,user_accoun)
        data = cr.fetchall()
        db.commit()
        db.close()

        return data[0][0]

def newPinChange(new_entered_pin,user_accoun):
        db = dbConnect()
        cr = db.cursor()
        t = (new_entered_pin,user_accoun)
        sql = "update user set pin=%s where accno=%s ;"
        cr.execute(sql,t)
        data = cr.fetchall()
        db.commit()
        db.close()

        x = OldPinCheck(user_accoun)

        new_entered_pin=int(new_entered_pin)
        if x == new_entered_pin:
            print("pinChange Sucess")
            return True
        else:
            print("pinChange Uncessfull")
            return False
# //*--------------//**//---------------------*//

#//*------------------PIN Genrate*------------------*//
def genOTP():
    # //*--Pin Change def is used to add new pin(i.e change NULL to New pin)
    otp = 0
    for i in range(1,5):
            otp = (otp*10) +rd.randint(0,9)

    return otp

# //*--------------//**//---------------------*//
#//*------------------Balance Enquiry-------------*//

def AccountType(acctype):
        db = dbConnect()
        cr = db.cursor()
        sql = "select acctype from user where accno=%s ;"
        cr.execute(sql,acctype)
        data = cr.fetchall()
        db.commit()
        db.close()
        return data[0]

def Pin_Bal(user_pin):
        db = dbConnect()
        cr = db.cursor()
        sql = "select pin from user where accno=%s ;"
        cr.execute(sql,user_pin)
        data = cr.fetchall()
        db.commit()
        db.close()

        pinmod = str(data[0][0])

        # //*--IF starting Number of pin is 0 then it does not shows in db
        if len(pinmod) == 3:
            updpin = "0"+str(pinmod)
            # print("gotpin",updpin)
            return updpin
        else:
            return data[0]

def ViewBalance(user_accoun):
        db = dbConnect()
        cr = db.cursor()
        sql = "select balance from user where accno=%s ;"
        cr.execute(sql,user_accoun)
        data = cr.fetchall()
        db.commit()
        db.close()

        return data[0][0]
# //*--------------//**//---------------------*//

#//*-------------Balance Enquiry-----------*//

# //*----------------CASH Withdrawl Note Management functions-------------**/
def getNotes():
    db = dbConnect()
    cr = db.cursor()
    atm_id = "101"
    sql = "select twoth,fivhun,twohun,onehun from note where atm_id=%s;"
    cr.execute(sql,atm_id)
    data = cr.fetchall()
    db.commit()
    db.close()
    return data[0]


#//*----------NOTES MANAGEMENT-----------------*//
def twoth(withd):

    note = getNotes()
    # print(note[4])
    notwot = note[0]
    nofivh = note[1]
    notwoh = note[2]
    noOnhun =note[3]
    totamu = (2000*note[0])+(500*note[1])+(200*note[2])+(100*note[3])
    # print("Total amount in ATM",totamu)
        #  getting note count
    req2000n = withd//(2000)
    #print("2000 note req : ",x)

    # note in atm minus rquired note
    remt=notwot-req2000n
    #print("atmNote-reqnote(2000) : ",remt)
    
    # finding mod of 2000 to pass remaining to five hundred
    modtwoth = withd%2000
    #print("amt to pass 500:",modtwoth)

    # if note is less in atm then the total required gets multiplied to 2000 and pass to the five hun
    if remt<0:
        passfiv = modtwoth - (remt*2000)
        print("tot to pass 500",passfiv)
        # final got note of 2000
        noOfTwoth = notwot 
        # print(noOfTwoth)
        # //*---Update 2000rs Note in SQL (setting it 0)--*//
        settingNote0("twoth")
  
    else:
        noOfTwoth = req2000n
        passfiv = modtwoth
        # print("2000",remt)
    # # //*---Update 2000rs Note in SQL--*//
        db = dbConnect()
        cr = db.cursor()
        atm_id = "101"
        t = (remt,atm_id)
        sql = "update note set twoth=%s where atm_id=%s;"
        cr.execute(sql,t)
        db.commit()
        db.close()

    # //*---------Five Hundred  NOTE----------**//

    req500n = passfiv//(500)
    remfiv=nofivh-req500n
    modfivhun = passfiv%500

    if remfiv < 0:

        passtwohun = modfivhun - (remfiv*500)
        noOffiv = nofivh
        # //*---Update 500rs Note in SQL (setting it 0)--*//
        settingNote0("fivhun")
  

        # if noOffiv !=0:
        #     return noOffiv
    else :
        passtwohun = modfivhun
        noOffiv = int(passfiv//(500))
        # print("500",remfiv)
        # # //*---Update 500rs Note in SQL--*//
        db = dbConnect()
        cr = db.cursor()
        atm_id = "101"
        s = (remfiv,atm_id)
        sql = "update note set fivhun=%s where atm_id=%s;"
        cr.execute(sql,s)
        db.commit()
        db.close()

 # //*---------Tw0 Hundred  NOTE----------**//

    #  getting note count
    req200n = passtwohun//(200)
    remtwoh=notwoh-req200n
    modtwohun = passtwohun%200

    if remtwoh<=0:
        passOnehun = modtwohun - (remtwoh*200)
        noOfTwoh = notwoh
        # //*---Update 200rs Note in SQL (setting it 0)--*//
        settingNote0("twohun")
  
    else:
        passOnehun = modtwohun
        # print("200",remtwoh)
        noOfTwoh = int(passtwohun//(200) )
        #  # //*---Update 200rs Note in SQL--*//
        db = dbConnect()
        cr = db.cursor()
        atm_id = "101"
        a = (remtwoh,atm_id)
        sql = "update note set twohun=%s where atm_id=%s;"
        cr.execute(sql,a)
        db.commit()
        db.close()
    
    # //*---------One Hundred  NOTE----------**//

    #  getting note count
    b = passOnehun//(100)
    remoneh=noOnhun-b

    if remoneh<=0:
        noOfOneh = remoneh
        # //*---Update 100rs Note in SQL (setting it 0)--*//
        settingNote0("onehun")
  

    else:
        noOfOneh = int(passOnehun//(100) )
        # print("100",remoneh)

        # # //*---Update 100rs Note in SQL--*//
        db = dbConnect()
        cr = db.cursor()
        atm_id = "101"
        b = (remoneh,atm_id)
        sql = "update note set onehun=%s where atm_id=%s;"
        cr.execute(sql,b)
        db.commit()
        db.close()

    # if remt>=0 and remfiv >=0 and remtwoh >=0 and remoneh >=0:
    if  remoneh < 0:
        # print("doing")
        db = dbConnect()
        cr = db.cursor()
        atm_id = "101"
        t = (note[0],note[1],note[2],note[3],atm_id )
        sql = "update note set twoth=%s, fivhun=%s, twohun=%s, onehun=%s where atm_id=%s;"
        cr.execute(sql,t)
        db.commit()
        db.close()

    return noOfTwoth,noOffiv,noOfTwoh,noOfOneh

# //*-------Update the Balance------*//
def updBalance(amount,user_accoun):
        db = dbConnect()
        cr = db.cursor()
        # atm_id = "101"
        t = (amount,user_accoun)
        sql = "update user set balance=%s where accno=%s;"
        cr.execute(sql,t)

        #//*-view updated balance and return it
        sql = "select balance from user where accno=%s;"
        cr.execute(sql,user_accoun)
        balance = cr.fetchall()
        db.commit()
        db.close()

        return balance[0]

def settingNote0(type):
        db = dbConnect()
        cr = db.cursor()
        atm_id = "101"
        t = ("0",atm_id)
        sql = f"update note set {type}=%s where atm_id=%s;"
        cr.execute(sql,t)
        db.commit()
        db.close()

# twoth(300)
# //*----------------------*****-----------------------**/

'''
NOTE QUeries
1. select twoth,fivhun,twohun,onehun, sum((2000*twoth)+(500*fivhun)+(200*twohun)+(100*onehun)) as total from note;
2. update note set twoth=2,fivhun=4,twohun=6,onehun=17 where atm_id="101";
3. select * from ministate where accno=12345 order by date desc;

'''


# //*----------------------MINI STATEMENT-----------------------**/
# //*----Function to ADD the CREDIT and Witdraw to the ministate table---*//
def addStatement(accno,type,amount):
        db = dbConnect()
        cr = db.cursor()
        CurDate = datetime.today().strftime("%y-%m-%d")
        print(CurDate)
        t = (accno,type,amount,CurDate)
        sql = "insert into ministate values(%s,%s,%s,%s)"
        cr.execute(sql,t)
        db.commit()
        db.close()

# //*----Function to get the MiniStatement-(Total)----*//
def getFullMiniStatement(accno):
        accoun = int(accno)
        print("Type of Accoun",type(accoun))
        db = dbConnect()
        cr = db.cursor()
        sql = "select * from ministate where accno=%s order by date desc limit 6;"
        cr.execute(sql,accoun)
        data = cr.fetchall()
        db.commit()
        db.close()

        return data

# //*----------------------*****-----------------------**/