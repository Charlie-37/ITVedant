ulist=[['Sunil', 'Male', '56000', 'sunilb', '1234', 3700, 5000], ['Prasad', 'male', '95000', 'prasadj', '9876', 29626, 0], ['Vidhi', 'female', '62000', 'vidhi', '1234', 3700, 0]]

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
         

    def showdetails(self):
        print(f"Name : {self.name.title()}")
        print(f"Gender : {self.gender.title()}")
        print(f"Salary : {self.salary}")
        print(f"Password : {self.passw}")
        print(f"Account Number : {self.accnum}")

    def addlist(self):
        newl = [self.name, self.gender, self.salary,self.passw,self.uadhar,self.accnum,self.__balance]
        ulist.append(newl)
        #print(ulist)


class bank(user):
    
    def __init__(self,name,gender,salary, upass, uadhar,acoun,bal):
        super().__init__(name,gender,salary,upass, uadhar)
        self.acoun = acoun
        self.__balance = bal
        

    def ulogin(self,ulist):
        #print(ulist)
        pass

    def viewbal(self):
        print("Balance is : ",end=" ")
        return self.__balance
    

    def deposite(self,dpamu):
        self.__balance = self.__balance + dpamu
        print("Money Deposited Sucessfully")
        #return f"current Balance is : {self.__balance} "
        return self.__balance

    def withdraw(self,withd):
        if withd > self.__balance:
            return print("InSufficient Balance")
        
        elif withd <= self.__balance and withd >= 100:
            self.__balance = self.__balance - withd
            print("Thank You Visit again")
            return self.__balance
        elif withd < 100:
            print("Please enter multiple of 100 \n Balance : {viewbal}")

    def amtf(self,amt,*tfacc):
        
        tfacc = list(tfacc)
        
        if amt> self.__balance:
            return print("Insufficient Balance")
        
        elif amt>=1 and amt<self.__balance:
            self.__balance = self.__balance - amt
            tfacc[6] = tfacc[6]+amt
            #tfacc.deposit(amt)
            print("Money Transfered Sucessfully")
            return self.__balance
            
        elif amt<1:
            print("Enter amount Greater than 1")
            
            

# //*----User Choice--------*//


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
            
            us = user(uname, ugen, usal, upass, uadhar)
            us.addlist()

            
            
            

        elif fchoi == "2":
            eacc = input("Enter Your Account Number : ").lstrip()
            eacc = int(eacc)
            epassw = input("Enter Your password : ").lstrip()

        

            for i in ulist:
                if eacc == i[5] and epassw == i[3]:
                    

                    while True:
                        print("\n")
                        print("Enter 1 for View Balance")
                        print("Enter 2 for Deposite")
                        print("Enter 3 for Withdraw")
                        print("Enter 4 for Amount Transfer")
                        print("Enter 5 for Exit")
                        print("\n")

                        achoi = input("Enter Your Choice : ").strip()


                        if achoi == "1":
                            #print(i)
                            obj1 = bank(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
                            print(obj1.viewbal())
                            

                        elif achoi == "2":
                            ados = input("Enter Amount To Deposit : ").strip()
                            ados = int(ados)
                            obj1 = bank(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
                            nbal = obj1.deposite(ados)
                            i[6] = nbal
                            print("\n")
                            print(obj1.viewbal())
                            print("\n")

                            


                        elif achoi == "3":
                            awithd = input("Enter Amount To Withdraw : ").strip()
                            awithd = int(awithd)
                            obj1 = bank(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
                            print("\n")
                            i[6] = obj1.withdraw(awithd)
                            print(obj1.viewbal())
                            

                        elif achoi == "4":
                            oacc = input("Enter Account Number To Transfer : ").strip()
                            oacc = int(oacc)

                            for j in ulist:
                                if oacc == j[5]:
                                    print(j)
                                    #print("Got Sender")
                                    amt = input("Enter Amount To Transfer : ").strip()
                                    amt = int(amt)
                                    obj1 = bank(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
                                    obj2 = bank(j[0],j[1],i[2],j[3],j[4],j[5],j[6])
                                    
                                    i[6]=obj1.amtf(amt,obj2)

                        elif achoi == "5":
                            firChoice(ulist)

                        else:
                            print("Invalid Input")
    ##                else:
    ##                    print("Invalid Details")
        
        
        #print(ulist)


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
