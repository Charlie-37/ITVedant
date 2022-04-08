ulist=[]

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
         

    def showdetails(self):
        print(f"Name : {self.name.title()}")
        print(f"Gender : {self.gender.title()}")
        print(f"Salary : {self.salary}")
        print(f"Password : {self.passw}")
        print(f"Account Number : {self.accnum}")
        


class bank(user):
    
    def __init__(self,name,gender,salary, upass, uadhar):
        super().__init__(name,gender,salary,upass, uadhar)
        self.__balance = 0

    def addlist(self):
        newl = [self.name,self.gender,self.salary,self.passw,self.uadhar,self.accnum,self.__balance]
        ulist.append(newl)
        #print(ulist)

    def ulogin(self,ulist):
        #print(ulist)
        pass

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
            
            
            
def firChoice(ulist):
    
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
            
            us = bank(uname, ugen, usal, upass, uadhar)
            us.addlist()

            
            
            

        elif fchoi == "2":
            
             print(ulist)


            # eaccoun = input("Enter Your Account Number : ").strip()
            # eaccoun  = int(eaccoun)
            # epassw = input("Enter Your Password : ").strip()



            

        else:
            print("Invalid Input")              


firChoice(ulist)


# obj1 = bank("sunil","male",20000)
# obj1.deposite(5000)

# print(obj1.viewbal())
# obj1.withdraw(100)

# print(obj1.viewbal())

# obj2 = bank("Prasad", "male", 25000)
# print(obj2.viewbal())
        
# obj1.amtf(2000,obj2)
# print(obj1.viewbal())
# print(obj2.viewbal())

# print(user.usercount)