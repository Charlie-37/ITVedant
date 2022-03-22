

class user():
    usercount = 0
    def __init__(self, name, gender, salary):
        self.name = name
        self.gender = gender
        self.salary = salary
        self.accnumber = "sbi@1"
        user.usercount+=1
         

    def showdetails(self):
        print(f"Name : {self.name.title()}")
        print(f"Gender : {self.gender.title()}")
        print(f"Salary : {self.salary}")


class bank(user):
    def __init__(self,name,gender,salary):
        super().__init__(name,gender,salary)
        self.__balance = 0
        
    def viewbal(self):
        return self.__balance
    
    def deposite(self,dpamu):
        self.__balance = self.__balance + dpamu
        return f"current Balance is : {self.__balance} "

    def withdraw(self,withd):
        if withd > self.__balance:
            return "InSufficient Balance"
        
        elif withd <= self.__balance and withd >= 100:
            self.__balance = self.__balance - withd
            return "Thank You Visit again"
        elif withd < 100:
            print("Please enter multiple of 100 \n Balance : {viewbal}")

    def amtf(self,amt,tfacc):
        if amt> self.__balance:
            return "Insufficient Balance"
        elif amt>=1:
            self.__balance = self.__balance - amt
            
            
        
            
        
        

obj1 = bank("sunil","male",20000)
obj1.deposite(5000)
print(obj1.viewbal())
obj1.withdraw(100)
print(obj1.viewbal())
        
