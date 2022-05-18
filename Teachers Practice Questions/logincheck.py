##
##userL = [["bhavesh","b123"],["tejas12","t1234"],["sunil23","sunil234"],["prasads23","pra123"]]
##
##def loginch(usname,upass,userL):
##
##    x = False
##    
##    for i in userL:
##        if usname==i[0] and upass == i[1]:
##            x = True
##
##
##    if x:
##        print("Sucess")
##
##    else:
##        print("Denied")
##
##
##loginch("sunil26522","sunil234",userL)



userL = [["bhavesh","b123"],["tejas12","t1234"],["sunil23","sunil234"],["prasads23","pra123"]]

def loginch(usname,upass,userL):
    listl = [usname,upass]

    if listl in userL:
        print("Sucess")

    else:
        print("denied")


##    for i in userL:
##        if usname==i[0] and upass == i[1]:
##            print("Sucess")
##        
##
##        else:
##            print("Denied")


loginch("sunil23","sunil234",userL)
