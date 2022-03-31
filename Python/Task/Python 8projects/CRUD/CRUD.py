
record= [
    
    (1,"Sunil",10,"Thane",2000),
    (2,"Bhavesh",23,"Karjat",300),
    (3,"Tejas",25,"Mulund",400),
    (4,"Prasad",22,"Nashik",500),
    (5,"Sandeep",24,"Badlapur",500)
    ]

def addRec(record):
    f = open("record.txt","x")
    for i,n,a,p,s in record:
        print(f"{i:^3} {n:^8} {a:^3} {p:^10} {s:^3}\n")
        f.write(f"{i:^3} {n:^8} {a:^3} {p:^10} {s:^4}\n")
    f.close()

#addRec(record)



def readRec(record):
    f = open("record.txt","r")
    for i,n,a,p,s in record:
        print(f"{i:^3} {n:^8} {a:^3} {p:^10} {s:^3}\n")
    f.close()

readRec(record)

def UpdateRec():
    f = open("record.txt","a")
    for i,n,a,p,s in record:
        f.write(f"{i:^3} {n:^8} {a:^3} {p:^10} {s:^4}\n")
    f.close()

