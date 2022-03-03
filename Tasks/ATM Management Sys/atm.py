from time import sleep
from playsound import playsound
import datetime
import time

# //*----------User Data------------------------------*//
user_data={
    90001:{
        "card_no": 90001,
        "name": "Sunil Bhave",
        "card_vdate": "09/22",
        "acc_ty":"saving",
        "pin":1234,
        "bal":5000
    },
    90002:{
        "card_no": 90002,
        "name": "Bhavesh Ainkar",
        "card_vdate": "04/21",
        "acc_ty":"saving",
        "pin":1254,
        "bal":7000
    },
    90003:{
        "card_no": 90003,
        "name": "Tejas Jhadav",
        "card_vdate": "07/22",
        "acc_ty":"current",
        "pin":1274,
        "bal":1200
    },
    90004:{
        "card_no": 90004,
        "name": "Sandeep Bind",
        "card_vdate": "10/23",
        "acc_ty":"saving",
        "pin":1894,
        "bal":15000
    },
    90005:{
        "card_no": 90005,
        "name": "Ankaj Yadav",
        "card_vdate": "08/22",
        "acc_ty":"saving",
        "pin":1234,
        "bal":4500
    },
      90006:{
        "card_no": 90006,
        "name": "Harshal Suryavanshi",
        "card_vdate": "08/22",
        "acc_ty":"saving",
        "bal":4500,

    }
}

# //*------------------ATM CASH NOTES-------------*//
notwot = 6
nofivh = 5
notwoh = 3
noOnhun = 10
totamu = (notwot*2000)+(nofivh*500)+(notwoh*200)+(noOnhun*100)

# //*----------------------------Creating Class-----------------------------*//

class atm_class:
    def __init__(self,en_acc_no,en_card_no,en_acc_ty,en_acc_pin) :
        self.en_acc_no = en_acc_no
        self.en_card_no = en_card_no
        self.en_acc_ty = en_acc_ty
        self.en_acc_pin = en_acc_pin
        #self.onehun = onehun


    #//*---------------------Getting account balance------------*//   
    #  
    def get_bal(self):
       balance =  user_data[self.en_acc_no]["bal"]
       return  balance

    #//*----------------New Pin Genration----------------------*//
    def new_pin_set(self):
    
        if "pin" in user_data[self.en_acc_no]:
            print("Pin Already Exists\n")
            user_atm()
           
        else:   
            new_pin = int(input("Enter New 4 digi pin : "))
            str_new_pin = str(new_pin)
            if len(str_new_pin) == 4:
                user_data[self.en_acc_no].setdefault("pin", new_pin)

                if user_data[self.en_acc_no]["pin"] == new_pin:
                    print("New Pin Created\n")
                    user_atm()
                else:
                    print("SomeThing went wrong")
                    user_atm()
                user_atm()
            else:
                print("Enter 4 digit Pin\n")

    #//*----------------------- Pin Updation-------------------------------------*//
    def upd_pin(self):

        if "pin" in user_data[self.en_acc_no]:
            upd_ex_pin = int(input("Enter New 4 digi pin : "))
            user_data[self.en_acc_no].update({"pin": upd_ex_pin})

            if user_data[self.en_acc_no]["pin"] == upd_ex_pin:
                print("Pin Updated\n")
                user_atm()
            else:
                print("SomeThing went wrong")
                user_atm()

        else:
            print("Pin does not exist Genrate your pin")
            user_atm()

    # //*-------------------Validating the pin After every while choice-------------------------*/

    def pin_valididation(self):
            en_acc_pin = int(input("\nEnter yor 4 digit pin : "))

            if "pin" in user_data[self.en_acc_no] :

                if user_data[self.en_acc_no]["pin"] == en_acc_pin:
                        print("Account pin Validated\n")
                        return True 
                             
                else:
                    return False
            else:
                print("No Pin Exists Please Genrate It\n")
                user_atm()

    # //*-------------------Cash Withdrawl-------------------------*/

    def cash_withd(self):
        withd = int(input("Enter Your Ammount : "))

        if withd %100 != 0:
            print("Multiple of 100, 200, 500 Only.")
            user_atm()
        else:
            if withd>10000:
                print("Only Maximum 10000 can Withdraw at a Time")
                user_atm()

            else:

                if withd>totamu:
                    print("Insuffecient Balance In ATM.")
                else:
                    if self.pin_valididation():
                        acc_bal = self.get_bal()

                        if withd > acc_bal:
                            print("Insuffecient Account Blance.")
                            user_atm()
                        else:
                            time.sleep(1)
                            #time.sleep(5)
                            # print("Take Your Cash & Don't Forget to get your card")
                            twoth(withd)
                            # # x = self.onehun
                            # # print(x)
                            # print("Avaliable Balance : ", acc_bal - withd,"\n")

                            noOfTwoth,noOffiv,noOfTwoh,noOfOneh = twoth(withd)

                            if noOfOneh < 0:
                                print("Please enter Multiple of 2000 and 500")
                                user_atm()
                            else:
                                #playsound('D:\SUNIL BHAVE\Documents\Coding\itvedant\Tasks\ATM Management Sys\cash.mp3')
                                playsound('audio\cash.mp3')
                                print("Take Your Cash & Don't Forget to get your card\n")

                                if noOfTwoth !=0:
                                    print("Note of 2000 :",noOfTwoth)
                                if noOffiv !=0:
                                    print("Note of 500 : ",noOffiv)
                                if noOfTwoh !=0:
                                    print("Note of 200 : ",noOfTwoh)
                                if noOfOneh !=0:
                                    print("Note of 100 : ",noOfOneh,"\n")
                                print("Avaliable Balance : ", acc_bal - withd,"\n")
                                user_atm()

# //*----------------------------****-----------------------------*//

# //*---------------Getting card details From User(Main Start Process)--------------**/


def user_atm():
    print("Please Enter Your Card details")
    en_acc_no = int(input("Enter Account Number : "))


    if en_acc_no in user_data.keys():
        print("Account Number validated\n")
        en_card_no = int(input("Enter Card Number : "))

        if user_data[en_acc_no]["card_no"] == en_card_no:
            
            print("Card Number validated\n")
            card_name = user_data[en_acc_no]["name"]
            print(f"Welcome {card_name} \n")
            en_acc_ty =input("Enter Account Type (Saving/Current): ")
            en_acc_ty = en_acc_ty.lower()


            if user_data[en_acc_no]["acc_ty"] == en_acc_ty:
                print("Account type Validated\n")

                # //*----Calling the Choice loop----**/
                acc_choi(en_acc_no,en_card_no,en_acc_ty)
                    
            else:
                print("Wrong Account type ")
                user_atm()
        else:
            print("Wrong Card Number")
            user_atm()
    else:
        print("Dose not exist")
        user_atm()

#//*-------------------------Creating atm choices---------------------*//

def acc_choi(en_acc_no,en_card_no,en_acc_ty) :
    while True:
        print("\nWelcome to Charlie's Bank \n")
        print("Enter 1 for Change Pin")
        print("Enter 2 for Genrate Pin")
        print("Enter 3 for Balance Enquery")
        print("Enter 4 for Mini Statement")
        print("Enter 5 for Cash Withdrawl")
        print("Enter 6 for Exit\n")
        
        en_choi = input("Enter Your Choices : ")

        if en_choi == "1":
            # //*----Require Sql database to change it   ---//
            print("Pin Change")

            chg_pin = atm_class(en_acc_no,en_card_no,en_acc_ty,'')
            if chg_pin.pin_valididation():
                chg_pin.upd_pin()

            else:
                print("Wrong Pin Enserted")
                user_atm()
            
        elif en_choi == "2":
            print("Genrate Pin ")
            new_pin = atm_class(en_acc_no,en_card_no,en_acc_ty,'')
            new_pin.new_pin_set()

        elif en_choi == "3":
            # //*----Pin Validating if true get balance
           
            pin_val = atm_class(en_acc_no,en_card_no,en_acc_ty,'')
            if pin_val.pin_valididation():
                print("balance Enquery ")
                account_bal = pin_val.get_bal()
                print("Your Account Balance is :", account_bal,"\n")
                user_atm()
            else:
                print("Wrong Pin\n")
                user_atm()        

        elif en_choi == "4":
            
        # //*----Pin Validating if true get balance science no log present same as bal enq

            pin_val = atm_class(en_acc_no,en_card_no,en_acc_ty,'')
            if pin_val.pin_valididation():
                print("balance Enquery ")
                pin_val.get_bal()
                user_atm()
            else:
                print("Wrong Pin\n")
                user_atm()

        elif en_choi == "5":

            cash_withdrawl = atm_class(en_acc_no,en_card_no,en_acc_ty,'')
            print("Cash Withdrawl")
            cash_withdrawl.cash_withd()
       
        elif en_choi == "6":
            print("exit ")
            break
            
#//*-------------------------***---------------------*//


# //*----------------CASH Withdrawl Note Management functions-------------**/

def twoth(withd):
        #  getting note count
    req2000n = withd//(2000)
    #print("2000 note req : ",x)

    # note in atm minus rquired note
    remt=notwot-req2000n
    #print("atmNote-reqnote(2000) : ",remt)
    
    # finding mod of 2000 to pass remaining to five hundred
    modtwoth = withd%2000
    #print("amt to pass 500:",modtwoth)

    # if note is less in atm then the total required gets multiplied to 2000 and pass to the five hun
    if remt<=0:
        passfiv = modtwoth - (remt*2000)
        #print("tot to pass 500",passfiv)
        # final got note of 2000
        noOfTwoth = notwot 
  
    else:
        noOfTwoth = req2000n
        passfiv = modtwoth

    # //*---------Five Hundred  NOTE----------**//

    req500n = passfiv//(500)
    remfiv=nofivh-req500n
    modfivhun = passfiv%500

    if remfiv <= 0:

        passtwohun = modfivhun - (remfiv*500)
        noOffiv = nofivh

        if noOffiv !=0:
            return noOffiv
    else:
        passtwohun = modfivhun
        noOffiv = int(passfiv//(500) )

 # //*---------Tw0 Hundred  NOTE----------**//

    #  getting note count
    req200n = passtwohun//(200)
    remtwoh=notwoh-req200n
    modtwohun = passtwohun%200

    if remtwoh<=0:
        passOnehun = modtwohun - (remtwoh*200)
        noOfTwoh = notwoh
    else:
        passOnehun = modtwohun
        noOfTwoh = int(passtwohun//(200) )
    
    # //*---------One Hundred  NOTE----------**//

    #  getting note count
    b = passOnehun//(100)
    remoneh=noOnhun-b
    if remoneh<0:
        noOfOneh = remoneh

    else:
        noOfOneh = int(passOnehun//(100) )
        
    return noOfTwoth,noOffiv,noOfTwoh,noOfOneh

# //*----------------------*****-----------------------**/


user_atm()







    

    
      



















    
