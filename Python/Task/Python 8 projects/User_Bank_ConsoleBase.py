

class user():
    
    
    usercount = 0
    def __init__(self, name, gender, salary, passw, adhar,balance):
        self.name = name
        self.gender = gender
        self.salary = salary
        self.passw = passw
        self.adhar = adhar
        self.accnum = int(adhar)*3-2
        self.balance = balance
        user.usercount+=1
         

    def showdetails(self):
        print("\n")
        print(f"Name : {self.name.title()}")
        print(f"Gender : {self.gender.title()}")
        print(f"Salary : {self.salary}")
        print(f"Password : {self.passw}")
        print(f"Account Number : {self.accnum}")

    def createUser(self):
        pass
            


class bank():
    ulist=[]
    
    def __init__(self):
        self.firChoice()
        self.__balance = 0

    
        
    def viewbal(self):
        print("Balance is : ",end=" ")
        return self.__balance
    

    def deposite(self,dpamu):
        self.__balance = self.__balance + dpamu
        print("Money Deposited Sucessfully")
        return f"current Balance is : {self.__balance} "

    def withdraw(self,withd):
        if withd > self.__balance:
            return "InSufficient Balance"
        
        elif withd <= self.__balance and withd >= 100:
            self.__balance = self.__balance - withd
            print("Thank You Visit again")
            return self.__balance
        elif withd < 100:
            print("Please enter multiple of 100 \n Balance : {viewbal}")

    def amtf(self,amt,tfacc):
        if amt> self.__balance:
            return "Insufficient Balance"
        elif amt>=1 and amt<self.__balance:
            self.__balance = self.__balance - amt
            tfacc.__balance = tfacc.__balance+amt
            #tfacc.deposit(amt)
            print("Money Transfered Sucessfully")
            
        elif amt<1:
            print("Enter amount Greater than 1")

    def firChoice(self):

        while True:
            
            print("\n")
            print("Enter 1 to Create Account")
            print("Enter 2 to Login Account")
            print("\n")

            fchoi = input("Enter Your Choice : ").strip()

            if fchoi == "1":
                uname = input("Enter Your Name : ").strip()
                ugen = input("Enter Your Gender : ").strip()
                usal = input("Enter Your Salary : ").strip()
                upass = input("Enter your Password : ").strip()
                uadhar = input("Enter Your Adhar Card No : ").strip()
                bal = self.__balance

                us = user(uname, ugen, usal, upass, uadhar,bal)
                self.ulist.append(us)
                us.showdetails()

                print("User Added Sucessfully")
                
                
                

            elif fchoi == "2":
                self.login()
                

            else:
                print("Invalid Input")

    def login(self):
        mainl = self.ulist
        #print(mainl)
        eacoun = input("Enter Your Account Number : ").strip()
        eacoun = int(eacoun)

        epass = input("Enter Your Password : ").strip()
        

        for i in self.ulist:
            
            if i.accnum == eacoun and i.passw == epass:
                print("Login Sucessful")
                print("\n")

                print("Enter 1 for View Balance")
                print("Enter 2 for Deposite")
                print("Enter 3 for Withdraw")
                print("Enter 4 for Amount Transfer")
                print("Enter 5 for Exit")
                print("\n")

                sechoi = input("Enter Your Choice : ").strip()

                if sechoi == "1":
                    #viewbal(self)
                    print("Balance is : ")
        

                elif sechoi == "2":
                    deposite(self)

                elif sechoi == "3":
                    withdraw(self)

                elif sechoi == "4":
                    amtf(self)

                elif sechoi == "2":
                    deposite()
                    

            else:
                print("Invalid")
            
                   

    ##obj1 = bank("sunil","male",20000)
##obj1.deposite(5000)
##
##print(obj1.viewbal())
##obj1.withdraw(100)
##
##print(obj1.viewbal())
##
##obj2 = bank("Prasad", "male", 25000)
##print(obj2.viewbal())
##        
##obj1.amtf(2000,obj2)
##print(obj1.viewbal())
##print(obj2.viewbal())
##
##print(user.usercount)



class userCreate():
    

    def __init__(self):
        
        self.firChoice()
        
    # //*---Loop For User Choice----*//

 





b = bank()





















    
    
