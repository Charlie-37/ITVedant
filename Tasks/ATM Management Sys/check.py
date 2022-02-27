

# from audioop import reverse
# from datetime import date
# td = date.today()


# ty = td.year
# tm = td.month

# cd = "01/2023"
# c1 = "02/2021"

# cs1 = cd[1:2]
# csy1 = cd[3::]


# if int(cs1)<tm or int(csy1)>ty:
#     print("true")

# print(0o2>7)




# notwot = 2
# nofivh = 5
# notwoh = 3
# noOnhun = 10
# totamu = (notwot*2000)+(nofivh*500)+(notwoh*200)+(noOnhun*100)

# withd = int(input("Enter Your Ammount : "))

















# # # //*---------Two THOUSAND NOTE----------**//
# def twoth():
#     #  getting note count
#     x = withd//(2000)
#     #print("2000 note req : ",x)

#     # note in atm minus rquired note
#     remt=notwot-x
#     #print("atmNote-reqnote(2000) : ",remt)
    
#     # finding mod of 2000 to pass remaining to five hundred
#     modtwoth = withd%2000
#     #print("amt to pass 500:",modtwoth)

#     # if note is less in atm then the total required gets multiplied to 2000 and pass to the five hun
#     if remt<=0:
#         passfiv = modtwoth - (remt*2000)
#         #print("tot to pass 500",passfiv)
        

#         # final got note of 2000
#         noOfTwoth = notwot 

#         if noOfTwoth != 0:
#             print("\nno of 2000 note",noOfTwoth,"\n")


#         fivhun(passfiv)
#     else:
#         passfiv = modtwoth
#         #print("amt to pass 500",passfiv)
        
    
#     # final got note of 2000
#         noOfTwoth = int(withd//(2000) )

#         if noOfTwoth !=0:
#             print("\nno of 2000 note :",noOfTwoth,"\n")

#         fivhun(passfiv)




# # //*---------Five Hundred  NOTE----------**//
# def fivhun(passfiv):
#     #  getting note count
#     y = passfiv//(500)
#     #print("req 500 note :",y)

#     # note in atm minus rquired note
#     remfiv=nofivh-y
#     #print("atmNote - reqnote(500): ",remfiv)
    
#     # finding mod of 2000 to pass remaining to five hundred
#     modfivhun = passfiv%500
#     #print("amt to pass 200 : ",modfivhun)

#     # if note is less in atm then the total required gets multiplied to 2000 and pass to the five hun
#     if remfiv<=0:
#         passtwohun = modfivhun - (remfiv*500)
#         #print("tot amt to pass 200 : ", passtwohun)

#         # final got note of 2000
#         noOffiv = nofivh

#         if noOffiv !=0:
#             print("no of 500 note :",noOffiv,"\n")
#         twohun(passtwohun)
#     else:
#         passtwohun = modfivhun
#         #print("Tot amt to pass 200 : ", passtwohun)
    
#     # final got note of 2000
#         noOffiv = int(passfiv//(500) )

#         if noOffiv !=0:
#             print("tot note of 500 : ", noOffiv,"\n")
#         twohun(passtwohun)
        


# # //*---------Twp Hundred  NOTE----------**//

# def twohun(passtwohun):
#     #  getting note count
#     a = passtwohun//(200)
#     #print("req 200 note :",a)

#     # note in atm minus rquired note
#     remtwoh=notwoh-a
#     #print("atmNote - reqnote(200): ",remtwoh)
    
#     # finding mod of 2000 to pass remaining to five hundred
#     modtwohun = passtwohun%200
#     #print("amt to pass 100 : ",modtwohun)

#     # if note is less in atm then the total required gets multiplied to 2000 and pass to the five hun
#     if remtwoh<=0:
#         passOnehun = modtwohun - (remtwoh*200)
#         #print("tot amt to pass 100 : ", passOnehun)

#         # final got note of 200
#         noOfTwoh = notwoh

#         if noOfTwoh !=0:
#             print("no of 200 note :",noOfTwoh,"\n")
#         onehun(passOnehun)
#     else:
#         passOnehun = modtwohun
#        # print("Tot amt to pass 100 : ", passOnehun)
    
#     # final got note of 2000
#         noOfTwoh = int(passtwohun//(200) )

#         if noOfTwoh !=0:
#             print("tot note of 200 : ", noOfTwoh,"\n")
#         onehun(passOnehun)



# # //*---------One Hundred  NOTE----------**//

# def onehun(passOnehun):
#     #  getting note count
#     b = passOnehun//(100)
#     #print("req 100 note :",b)

#     # note in atm minus rquired note
#     remoneh=noOnhun-b
#     #print("atmNote - reqnote(100): ",remoneh)
    
#     # finding mod of 2000 to pass remaining to five hundred
#     modOnehun = passOnehun%100
#     #print("amt to pass 100 : ",modOnehun)

#     # if note is less in atm then the total required gets multiplied to 2000 and pass to the five hun
#     if remoneh<=0:
#         print("Insufficient Balance")
#     else:
       
    
#     # final got note of 2000
#         noOfOneh = int(passOnehun//(100) )

#         if noOfOneh !=0:
#             print("tot note of 100 : ", noOfOneh,"\n")



# if withd%100 != 0:
#     print("Multiple of 100, 200, 500 Only.")
# else:
#     if withd>10000:
#         print("Only Maximum 10000 can Withdraw at a Time")
    
#     else:

#         if withd>totamu:
#             print("Insuffecient Balance In ATM.")
#         else:
#             twoth()


from playsound import playsound
playsound('D:\SUNIL BHAVE\Documents\Coding\itvedant\Tasks\ATM Management Sys/cash.mp3')
