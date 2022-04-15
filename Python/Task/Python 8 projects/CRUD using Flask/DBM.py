import pymysql as p
def getConnection():
    return p.connect(host='localhost',user='root',password='',database='pythonlect')
    
def addEmp(t):
    db=getConnection()
    sql='insert into crudflask values(%s,%s,%s,%s,%s)'
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()



def selectAllEmp():
    db=getConnection()
    sql='select * from crudflask'
    cr=db.cursor()
    cr.execute(sql)
    elist=cr.fetchall()
    db.commit()
    db.close()
    return elist

def login_page():
    db=getConnection()
    sql='select name, passw from crudflask'
    cr=db.cursor()
    cr.execute(sql)
    elist2=cr.fetchall()
    db.commit()
    db.close()
    return elist2

    
def deleteEmp(id):
    db=getConnection()
    sql='delete from  crudflask where id=%s'
    cr=db.cursor()
    cr.execute(sql,id)
    db.commit()
    db.close()

def selectEmpById(id):
    db=getConnection()
    sql='select * from crudflask where id=%s'
    cr=db.cursor()
    cr.execute(sql,id)
    elist=cr.fetchall()
    db.commit()
    db.close()
    return elist[0]

def updateEmp(t):
    db=getConnection()
    sql='update crudflask set name=%s,contact=%s,email=%s,passw=%s where id=%s'
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()
