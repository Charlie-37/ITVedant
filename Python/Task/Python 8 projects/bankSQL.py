
import pymysql as p

# //*-------MYSQL Connectivity---------*//

# //*--Function to Db Connectivity----*//
def dbConnect():
    return p.connect(host="localhost", user="root",password="",database="pythonlect")


# //*-------Class to create and Show User Details-----------*//
class user():
    usercount = 0
    def __init__(self, name, gender, salary,upass, uadhar):
        self.name = name
        self.gender = gender
        self.salary = salary
        self.passw = upass
        self.uadhar = uadhar
        self.accnum = int(uadhar)*3-2
        user.usercount+=1
        self.__balance = 0
         

    def addlist(self):
        newl = (self.name, self.gender, self.salary,self.passw,self.uadhar,self.accnum,self.__balance)
        db = dbConnect()
        cr = db.cursor()

        sql = "insert into userbank values(%s,%s, %s, %s, %s, %s, %s)"
        cr.execute(sql,newl)
        print("added Sucessfully")

        data = cr.fetchall()

        db.commit()
        db.close()

        return data


    def showdetails(self):
        
        db = dbConnect()
        cr = db.cursor()

        sql = "select * from userbank where accountNo = %s"
        cr.execute(sql,self.accnum)

        data = cr.fetchall()

        db.commit()
        db.close()
        
        for i in data:
            return i 

# //*---------Class for Bank Transactions-----------*//
class bank(user):
    
    def __init__(self,name,gender,salary, upass, uadhar,acoun,bal):
        super().__init__(name,gender,salary,upass, uadhar)
        self.acoun = acoun
        self.__balance = bal

    # //*----Function to View Balance------*//  

    def viewbal(self):
        db = dbConnect()
        cr = db.cursor()

        sql = "select balance from userbank where accountNo = %s"
        cr.execute(sql,self.acoun)

        data = cr.fetchall()
        
        db.commit()
        db.close()

        data = list(data)
        return data[0][0]

    # //*----Function to Deposite Money------*// 

    def deposite(self,dpamu):
        self.__balance = self.__balance + dpamu
        db=dbConnect()
        cr = db.cursor()

        t = (self.__balance,self.acoun)
        sql = "update userbank set balance = %s where accountNo=%s"

        cr.execute(sql,t)

        db.commit()
        db.close()

        print("Money Deposited Sucessfully")

        return self.__balance

    # //*----Function to Withdraw Money------*// 

    def withdraw(self,withd):
        db = dbConnect()
        cr = db.cursor()

        sql = "select balance from userbank where accountNo = %s"
        cr.execute(sql,self.acoun)

        data = cr.fetchall()
        db.commit()
        db.close()
        
        data = list(data)
        livbal = data[0][0]
        
        if withd > livbal:
            return print("InSufficient Balance")
        
        elif withd <= livbal and withd >= 100:
            livbal = livbal - withd
            db = dbConnect()
            cr = db.cursor()

            t = (livbal,self.acoun)
            sql = "update userbank set balance = %s where accountNo=%s"

            cr.execute(sql,t)

            db.commit()
            db.close()
            print("Thank You Visit again")
            return livbal

        
        elif withd < 100:
            print("Please enter multiple of 100 ")

    # //*--------Function to Transfer Money---------*// 
    def amtf(self,tfacc):

        db = dbConnect()
        cr = db.cursor()

        sql = "select * from userbank"
        cr.execute(sql)

        data = cr.fetchall()
        db.commit()
        db.close()
        
        for i in data:
            if tfacc == i[5]:
                amt = input("Enter Ammount To Transfer : ").strip()
                amt = int(amt)

                if amt> self.__balance:
                    return print("Insufficient Balance")
                
                elif amt>=1 and amt<self.__balance:
                        tbal = i[6]
                        tbal = tbal + amt
                        db = dbConnect()
                        cr = db.cursor()
                        t = (tbal,tfacc)

                        sql = "update userbank set balance = %s where accountNo = %s"
                        cr.execute(sql,t)

                        db.commit()
                        db.close()

                        print("\nMoney Transfered Sucessfully")
                        db = dbConnect()
                        cr = db.cursor()

                        self.__balance = self.__balance - amt
                        t = (self.__balance,self.acoun)
                        sql = "update userbank set balance = %s where accountNo=%s"

                        cr.execute(sql,t)

                        db.commit()
                        db.close()
                               
                elif amt<1:
                    print("Enter amount Greater than 1") 
            

# //*----User Choice--------*//


def firChoice():
    
    while True:
        
        print("\n")
        print("Enter 1 to Create Account")
        print("Enter 2 to Login Account")
        print("\n")

        fchoi = input("Enter Your Choice : ").strip()

        if fchoi == "1":
            uname = input("Enter Your Name : ").strip().title()
            ugen = input("Enter Your Gender : ").strip().title()
            usal = input("Enter Your Salary : ").strip()
            upass = input("Enter your Password : ").strip()
            uadhar = input("Enter Your Adhar Card No : ").strip()
            
            us = user(uname, ugen, usal, upass, uadhar)
            us.addlist()       

        elif fchoi == "2":
            eacc = input("Enter Your Account Number : ").lstrip()
            eacc = int(eacc)
            epassw = input("Enter Your password : ").lstrip()

            db = dbConnect()
            cr = db.cursor()

            sql = "select * from userbank"
            cr.execute(sql)

            data = cr.fetchall()

            
            db.commit()
            db.close()

            for i in data:
                if eacc == i[5] and epassw == i[3]:
                    
                    while True:
                        print("\n")
                        print("Enter 1 for View Balance")
                        print("Enter 2 for Deposite")
                        print("Enter 3 for Withdraw")
                        print("Enter 4 for Amount Transfer")
                        print("Enter 5 to Show Details")
                        print("Enter 6 for Exit")
                        print("\n")

                        achoi = input("Enter Your Choice : ").strip()

                        if achoi == "1":
                            #print(i[5])
                            obj1 = bank(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
                            balan = obj1.viewbal()
                            print(f"Balance is : {balan} Rs ")
                            print("\n")
                            
                        elif achoi == "2":
                            ados = input("Enter Amount To Deposit : ").strip()
                            ados = int(ados)
                            obj1 = bank(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
                            obj1.deposite(ados)

                            print("\n")
                            balan = obj1.viewbal()
                            print(f"Balance is : {balan} Rs ")
                            print("\n")

                        elif achoi == "3":
                            awithd = input("Enter Amount To Withdraw : ").strip()
                            awithd = int(awithd)
                            obj1 = bank(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
                            print("\n")
                            obj1.withdraw(awithd)
                            balan = obj1.viewbal()
                            print(f"Balance is : {balan} Rs ")
                            print("\n")
                            

                        elif achoi == "4":
                            tfacc = input("Enter Account Number To Transfer : ").strip()
                            tfacc = int(tfacc)

                            obj1 = bank(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
                            obj1.amtf(tfacc)
                            
                            balan = obj1.viewbal()
                            print(f"Balance is : {balan} Rs ")
                            print("\n")

                        elif achoi == "5":
                            obj1 = user(i[0],i[1],i[2],i[3],i[4])
                            i = obj1.showdetails()

                            print(f"Name : {i[0].title()}")
                            print(f"Gender : {i[1].title()}")
                            print(f"Salary : {i[2]}")
                            print(f"Password : {i[3]}")
                            print(f"Aadhar Card Number : {i[4]}")
                            print(f"Account Number : {i[5]}")
                            print(f"Account Balance : {i[6]}")

                        elif achoi == "6":
                            firChoice()




            

        else:
            print("Invalid Input")              

firChoice()
