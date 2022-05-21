
# //*-----Highest number----*//
list1 = [1,2,54,456,87,34,99,960,955]

def high(list1):
    num = -999999
    for i in list1:
        if i%2 !=0:
            if i > num:
                num = i
    print(num)
#high(list1)



# //*----Vovels----*//

list2 = ["sunil", "bhavesh", "tejas", "xyzk","sujay","ujay", "lkip"]

def vovl(list2):
    vollist = []
    for i in list2:
        vol = ["a","e","i","o","u"]
        
        for j in i:
            if j in vol:
                vollist.append(i)
                break
            
    print(vollist)
#vovl(list2)


# list2 = ["sunil", "bhavesh", "tejas", "xyzk","sujay","ujay", "lkip"]

# def vovl2(list2):
#     vollist = []
#     x=['a','e','i','o','u']
#     for a in list2:
#         for k in x:
#             if k in a:
#                 print(a)
#                 break;

# vovl2(list2)

def tab(n,i=1):
    if i <= 10:
        x = n * i

        print(n,"*",i,"=",x)
        return tab(n,i+1)
        
#tab(8)

# class emp():
#     empCount = 0

#     def __init__(s):
#         emp.empCount +=1
#         s.id = 0
#         pass

#     def empId(s):
#         id = 0

#         return id


    

# emp1 = emp()
# print(emp1.empCount)
# print(emp1.empId())

# emp2 = emp()
# print(emp2.empCount)
# print(emp2.empId())

# emp3 = emp()
# print(emp3.empCount)
# print(emp3.empId())

# class A :
#     x = 0
#     y = 0

#     def show(s):
#         s.x += 1
#         A.y +=1

#         print(s.x, A.y)


# a = A
# a.show()
# a.show()
# a.show()


# //*----EMP Detailsss-*//

l1 = ["Sunil","sunil@123", 25000,"TCS",2]
l2 = ["Bhavesh","bhavesh@123", 29000,"Wipro",3]
l3 = ["Tejas","teja@123", 35000,"Capg",1]

name = input("Input Name : ")
Email = input("Input Email : ")
Salary = int(input("Input Salary : "))
company = input("Input company : ")
age = int(input("Input AGE : "))
WE = int(input("Input WE : "))


class emp():
    def __init__(s,name,Email,Salary,company,age,WE):
        s.name = name
        s.email = Email
        s.sal = Salary
        s.age = age
        s.company = company
        s.we = WE

    def show(s):
        totsal = s.sal * 12*s.we
        epf = (s.sal/100)*12

        if s.we < 3:
            bonus = (s.sal/100) * 18

        elif s.we >= 3 and s.we < 5:
            bonus = (s.sal/100) * 22

        elif s.we >= 5 :
            bonus = (s.sal/100) * 25

        print("\n")
        print("Name : ", s.name)
        print("Email : ", s.email)
        print("Salary : ", s.sal)
        print("Age : ", s.age)
        print("Company : ", s.company)
        print("Work Exp : ", s.we)
        print("Anual Salary : ", totsal)
        print("PF : ", epf)
        print("Bonus : ", bonus)


y = emp(name,Email,Salary,company,age,WE)
y.show()