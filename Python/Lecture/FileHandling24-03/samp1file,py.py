
# //*--- File Reading-------*//

def read1():
    file=open("samp1.txt","r")
    cont = file.read()
    print(cont)
    file.close()


#read1()


record= [
    
    (1,"Sunil",10,"Thane",2000),
    (2,"Bhavesh",23,"Karjat",300),
    (3,"Tejas",25,"Mulund",400),
    (4,"Prasad",22,"Nashik",500),
    (5,"Sandeep",24,"Badlapur",500)
    ]


def addrec(record):
    file = open("log.txt","w")
    for i,n,a,p,s in record:
        print(f"{i:^3} {n:^8} {a:^3} {p:^10} {s:^3}\n")
        file.write(f"{i:^3} {n:^8} {a:^3} {p:^10} {s:^4}\n")
    file.close()

#addrec(record)


def appendtxt():
    file = open("samp1.txt","a")
    file.write("\nthis is Appended Scentence")
    file.close()
        
#appendtxt()



with open("samp1.txt","r") as file:
    cont = file.read()
    #print(cont)




def delList(record,n,addrec):
    del record[n]
    addrec(record)



#delList(record,3,addrec)

database = [
    ("jay",111),
    ("raj",222),
    ("suraj",333)
    ]

a = "raj"
b = 222

for i,j in database:
    if i==a and j==b:
        print("sucess")
        
    else:
        print("lol")
        

    














