 
Class user(): 
    Usercount = 0 
    Def __init__(self, name, gender, salary): 
        Self.name = name 
        Self.gender = gender 
        Self.salary = salary 
        Self.accnumber = “sbi@1” 
        User.usercount+=1 
       

 Def showdetails(self): 
     Print(f”Name : {self.name.title()}”) 
     Print(f”Gender : {self.gender.title()}”) 
     Print(f”Salary : {self.salary}”) 
  
  
 Class bank(user): 
     Def __init__(self,name,gender,salary): 
         Super().__init__(name,gender,salary) 
         Self.__balance = 0 
          
     Def viewbal(self): 
         Return self.__balance 
      
     Def deposite(self,dpamu): 
         Self.__balance = self.__balance + dpamu 
         Return f”current Balance is : {self.__balance} “ 
  
     Def withdraw(self,withd): 
         If withd > self.__balance: 
             Return “InSufficient Balance” 
          
         Elif withd <= self.__balance and withd >= 100: 
             Self.__balance = self.__balance – withd 
             Return “Thank You Visit again” 
         Elif withd < 100: 
             Print(“Please enter multiple of 100 \n Balance : {viewbal}”) 
  
     Def amtf(self,amt,tfacc): 
         If amt> self.__balance: 
             Return “Insufficient Balance” 
         Elif amt>=1: 
             Self.__balance = self.__balance – amt 
              
              
          
              
          
          
  
 Obj1 = bank(“sunil”,”male”,20000) 
 Obj1.deposite(5000) 
 Print(obj1.viewbal()) 
 Obj1.withdraw(100) 
 Print(obj1.viewbal())
