
import json
from datetime import datetime
import time
from flask import *
from bankdb import *


app = Flask(__name__)
app.secret_key = "hello"
# //*--Home Page----
@app.route("/")

def home():
    return render_template("home.html")

# //*-----------User Regestration----------*//
@app.route("/usersignIn")

def Usersign_In():
    return render_template("usersignin.html")


# //*-----------staff Regestration------------*//
@app.route("/staffsignIn")

def Staffsign_In():
    return render_template("staffsignin.html")


# //*------------Adding user details-------------*//
@app.route("/adduser", methods=["POST"])
def add_user():
    fname = request.form["user_first_name"]
    lname = request.form["user_last_name"]
    usname = request.form["user_username"]
    passw = request.form["user_password"]
    contact = request.form["user_contact"]
    adhar = request.form["user_aadhar"]
    city = request.form["user_city"]
    dob = request.form["user_dob"]
    acctype = request.form["user_acc_type"]
    gender = request.form["user_gen"]

    usercr = userdet(fname, lname, usname, passw, contact, adhar, city, dob, acctype, gender)
    usercr.cruser()

    return redirect("/")



# //*---------------Login User----------------*//

@app.route("/loginuser", methods=["POST"])
def User_login():
    usname = request.form["login_user_name"]
    passw = request.form["login_user_pass"]

    passid = user_login()

    if((usname,passw) in passid):
        t = (usname,passw)
        i = selectuser(t)
        i = list(i)

        session["user"] = i
        print(i)
        return render_template("showuser.html", row=i)
        
    else:
        return redirect("/")

# //*------------Show user details-------------*//
@app.route("/showuser")
def show_user():
    user = session["user"]
    # print(i)
    return render_template("showuser.html", row=user)


# //*------------Update user details-------------*//
@app.route("/upduser", methods=["POST"])
def update_user():
    fname = request.form["user_first_name"]
    lname = request.form["user_last_name"]
    usname = request.form["user_username"]
    passw = request.form["user_password"]
    contact = request.form["user_contact"]
    adhar = request.form["user_aadhar"]
    city = request.form["user_city"]
    dob = request.form["user_dob"]
    acctype = request.form["user_acc_type"]
    gender = request.form["user_gen"]
    accoun = request.form["user_accoun"]

    user1 = userdet(fname, lname, usname, passw, contact, adhar, city, dob, acctype, gender)
    user1.updateUser(accoun)
    # print(t)
    # updateUser(t)

    return redirect("/")


# //*------------Deposite Money(page render)-----*//
@app.route("/deposite")
def depo_Money():
    user = session["user"]
    return render_template("deposite.html",row=user)

#//*----------deposite(logic)--------*//

@app.route("/deposit_from", methods=["POST"])
def dep_money():
    accoun = request.form["deposite_account"]
    passw = request.form["deposite_passw"]
    amount = request.form["deposite_ammount"]

    x = deposite_money(accoun,passw,amount)

    if x == True:
        print("Sucess")
        addStatement(accoun,"cr",amount)
        return redirect("/deposite")

    else:
        print("unsucess")
        return redirect("/deposite")


#//*----------LOGOUT User------------*//
@app.route("/logout")
def user_log_out():
    session.pop("user",None)
    return redirect("/")

#//*----------Money Transfer(Page render)--------*// 
@app.route("/userMoneyTransfer")
def tff_amount():
    user = session["user"]
    return render_template("usermoneytff.html",row=user)

#//*----------Money Transfer(logic)--------*// 

@app.route("/MoneyTransfer_form", methods=["POST"])
def transfer_money():
    user_accoun = request.form["user_account"]
    passw = request.form["user_passw"]
    amount = request.form["transfer_ammount"]
    payee_accoun = request.form["Payee_account"]

    x = transferMoney(user_accoun,passw,amount,payee_accoun)
    addStatement(user_accoun,"dr",amount)
    return redirect("userMoneyTransfer")
    








#//**-------------------STAFF Methods------------*//



# //*---Adding Staff details----*//
@app.route("/addstaff", methods=["POST"])
def add_staff():
    fname = request.form["staff_first_name"]
    lname = request.form["staff_last_name"]
    usname = request.form["staff_username"]
    passw = request.form["staff_password"]
    contact = request.form["staff_contact"]
    adhar = request.form["staff_aadhar"]
    city = request.form["staff_city"]
    dob = request.form["staff_dob"]
    pos = request.form["staff_pos"]
    gender = request.form["staff_gen"]

    staffcr = staffdet(fname, lname, usname, passw, contact, adhar, city, dob, pos, gender)
    staffcr.crstaff()
    t = (fname, lname, usname, passw, contact, adhar, city, dob, pos, gender)
    print(t)
    return redirect("/")


# //*-------------Login staff------------*//

@app.route("/loginstaff", methods=["POST"])
def Staff_login():
    usname = request.form["login_staff_name"]
    passw = request.form["login_staff_pass"]

    passid = staff_login()

    if((usname,passw) in passid):
        t = (usname,passw)
        j = selectstaff(t)
        session["staff"] = j
        
        return render_template("/showstaff.html", row=j)
    else:
        return redirect("/")



# //*------------Show staff details-------------*//
@app.route("/showstaff")
def show_staff():
    staff = session["staff"]
    # print(i)
    return render_template("showstaff.html", row=staff)



# //*--staff update details---*//
@app.route("/updatestaff", methods = ["POST"])
def update_staff():
    accoun = request.form["staff_accoun"]
    fname = request.form["staff_first_name"]
    lname = request.form["staff_last_name"]
    usname = request.form["staff_username"]
    passw = request.form["staff_password"]
    contact = request.form["staff_contact"]
    adhar = request.form["staff_aadhar"]
    city = request.form["staff_city"]
    dob = request.form["staff_dob"]
    pos = request.form["staff_pos"]
    gender = request.form["staff_gen"]

    t = (fname, lname, usname, passw, contact, adhar, city, dob, pos, gender, accoun)
    print(t)
    return redirect("/")
# //*-------User List-----------*//

@app.route("/userList")
def user_list():
    user_data = selectAllUser()
    return render_template("userlist.html", ulist = user_data)

# //*-------EDIT User BY Staff-----------*//
@app.route("/editUserByStaff")

def editBy_staff():
    accnum = request.args.get("accoun")
    # print("accno is",accnum)
    data = selectuser_staff(accnum)
    return render_template("updateUserByStaff.html", row=data)


# //*-------delete User BY Staff-----------*//
@app.route("/delUserByStaff")
def delby_staff():
    accnum = request.args.get("accoun")
    print("accno is",accnum)
    deleteuser_staff(accnum)
    return redirect("userList")



#//*----------LOGOUT User------------*//
@app.route("/stafflogout")
def staff_log_out():
    session.pop("staff",None)
    return redirect("/")




#//*--------------------------ATM Starting-------------------*//

# //*-----------ATM main Page-----------*//
@app.route("/atmMain")
def atm_mainpage():
    return render_template("atm.html")


@app.route("/AtmAccCvv", methods=["POST"])
def atm_cvv():
    accoun = request.form["user_acoun"]
    accCvv = request.form["user_cvv"]

    # print("account is",accoun,accCvv)
    data = Atmaccdet(accoun,accCvv)
    if data != None:
        session["atm"] = data
        return render_template("atmChoice.html")
    else:
        return redirect("/")


#//*---Main Starting Choice----*//
@app.route("/atmlogout")
def atmlog():
    session.pop("atm",None)
    return redirect("/")


# //*--------------------First Selection------------------*//
@app.route("/first_select", methods=["POST"])
def main_choi():
    firChoi = request.form["main_choice"]
    # print("choice is",firChoi)
    if firChoi == "PinChange":
        return render_template("/PinChange.html")

    elif firChoi == "MiniStatement":
        return render_template("MiniStateAccTypeCheck.html")

    elif firChoi == "Withdrawl":
        return render_template("withdAccTypeCheck.html")

    elif firChoi == "BalanceEnquiry":
        # data = session["atm"]
        # bal = data[10]
        # bal = int(bal)
        return render_template("AccTypeCheck.html")

    elif firChoi == "GenratePin":

        data = session["atm"]
        accoun = data[11]
        pin = Pin_Bal(accoun)
        pin = pin[0]

        if pin == None:
            otp = genOTP()
            print("OTP IS : ", otp)
            session["otp"] = otp
            return render_template("/GenratePin.html")
        else:
            session.pop("atm",None)
            return redirect("/")

    else:
        print("Invalid Choice")
        session.pop("atm",None)
        return redirect("/")


#//*--------------------PIN Change--------------*//
@app.route("/pinChange_old", methods=["POST"])
def old_pin():
    old_entered_pin = request.form["acc_old_pin"]

    data = session["atm"]
    user_accoun = data[11]
    x = OldPinCheck(user_accoun)

    if x!= None:
        x = str(x)
        if len(x) == 3:
            x = "0"+str(x)
        else:
            pass

        print("final pin" , x)
        return render_template("pinChangeNewPin.html")
    else:
        print("Invalid")
        session.pop("atm",None)
        return redirect("/")

@app.route("/pinChange_new", methods=["POST"])
def new_pin():
    new_entered_pin = request.form["acc_new_pin"]

    data = session["atm"]
    user_accoun = data[11]
    newPinChange(new_entered_pin,user_accoun)

    session.pop("atm",None)
    return redirect("/")


#//*--------------PIN Genrate--------------*//
@app.route("/genPin_otp", methods=["POST"])
def PinGen_otp():
    entered_otp = request.form["genPin_otp"]
    entered_otp = int(entered_otp)
    data = session["atm"]
    user_accoun = data[11]

    otp = session["otp"]

    if entered_otp == otp:
        session.pop("otp",None)
        return render_template("/newPinGenrate.html")
    else:
        
        session.pop("atm",None)
        session.pop("otp",None)

        return redirect("/")

@app.route("/genrate_newpin", methods=["POST"])
def genNew_Pin():
    enter_genPin = request.form["acc_new_Genpin"]

    data = session["atm"]
    user_accoun = data[11]
    newPinChange(enter_genPin,user_accoun)
    session.pop("atm",None)
    return redirect("/")

#//*----------BALANCE Enquiry--------------*//
@app.route("/AcctypeCheck", methods=["POST"])
def ACC_Type():
    accty = request.form["acc_type"]

    data = session["atm"]
    user_acctype = data[11]
    x = AccountType(user_acctype)

    if x[0] == accty:
        return render_template("/PinCheck.html")
    else:
        print("Invalid")
        session.pop("atm",None)
        return redirect("/")


# //*---------Pin Check--------------*//

@app.route("/pinCheck", methods=["POST"])
def PIN_Check():
    enter_pin = request.form["acc_pin"]

    data = session["atm"]
    user_accoun = data[11]
    x = Pin_Bal(user_accoun)
    

    print("user given",enter_pin)
    print("user ",x)
    if enter_pin == x:
        print("sucess")
        bal = ViewBalance(user_accoun)
        return render_template("/viewbal.html" , balance=bal)
    else:
        print("Invalid")
        session.pop("atm",None)
        return redirect("/")


@app.route("/exit_bal", methods=["POST"])
def exit_balance():
        session.pop("atm",None)
        return redirect("/")


# //*---------------------WithDrawl-------------------------*//

#//*---Redirected to Account Type Check(used balanceEnquery's type check)
@app.route("/withdAcctypeCheck", methods=["POST"])
def ACCtype_Type():
    accty = request.form["acc_type"]

    data = session["atm"]
    user_acctype = data[11]
    x = AccountType(user_acctype)

    if x[0] == accty:
        return render_template("/withdPinCheck.html")
    else:
        print("Invalid")
        session.pop("atm",None)
        return redirect("/")

# //*---------Pin Check--------------*//

@app.route("/withdpinCheck", methods=["POST"])
def enteredPin_Check():
    enter_pin = request.form["acc_pin"]

    data = session["atm"]
    user_accoun = data[11]
    x = Pin_Bal(user_accoun)
    

    print("user given",enter_pin)
    print("user ",x)
    if enter_pin == x:
        print("sucess")

        return render_template("/enterAmount.html")
    else:
        print("Invalid")
        session.pop("atm",None)
        return redirect("/")

#//*---------------------CASH Withdrawl Process-------------*//


@app.route("/enterAmount", methods=["POST"])
def entered_amount():
    withd = request.form["ent_amount"]

    data  = session["atm"]
    user_accoun = data[11]
    # //*--Used finction from Balance Enquiry(ViewBalance)
    acc_bal = ViewBalance(user_accoun)

    print("acc_bal type",type(acc_bal))
    withd = int(withd)
    print("withd amt",type(withd))
    updbalance = acc_bal - withd

    note = getNotes()
    totamu = (2000*note[0])+(500*note[1])+(200*note[2])+(100*note[3])

    if withd>10000:
        print("Only Maximum 10000 can Withdraw at a Time")
        session.pop("atm",None)
        return redirect("/")

    else:

        if withd>totamu:
            print("Insuffecient Balance In ATM.")
            session.pop("atm",None)
            return redirect("/")
        else:
            if withd > acc_bal:
                print("Insuffecient Account Blance.")
                session.pop("atm",None)
                return redirect("/")

            else:
                time.sleep(1)
                #time.sleep(5)
                # print("Take Your Cash & Don't Forget to get your card")
                # # x = self.onehun
                # # print(x)
                # print("Avaliable Balance : ", acc_bal - withd,"\n")

                noOfTwoth,noOffiv,noOfTwoh,noOfOneh = twoth(withd)

                if noOfOneh < 0:
                    print("Please enter Multiple of 2000 and 500")
                    session.pop("atm",None)
                    return redirect("/")
                else:
                    #playsound('D:\SUNIL BHAVE\Documents\Coding\itvedant\Tasks\ATM Management Sys\cash.mp3')
                    #playsound('cash.mp3')
                    print("Take Your Cash & Don't Forget to get your card\n")

                    # //*--Update the User'sBalance

                    balance = updBalance(updbalance,user_accoun)
                    balance= balance[0]
                    Notes = [noOfTwoth,noOffiv,noOfTwoh,noOfOneh,balance]
                    addStatement(user_accoun,"dr",withd)
                    session.pop("atm",None)
                    return render_template("ViewWithdrawl.html", note = Notes)

@app.route("/Withdlogout", methods=["POST"])
def Withd_logout():
        
    session.pop("atm",None)
    return redirect("/")

#//*---------------------MINI STATEMENT-------------*//

#//*---ACC Type Check----------*//
@app.route("/MiniStateAcctypeCheck", methods=["POST"])
def MiniACCtype_Type():
    accty = request.form["acc_type"]

    data = session["atm"]
    user_acctype = data[11]
    x = AccountType(user_acctype)

    if x[0] == accty:
        # print("gottt")
        return render_template("/MiniStatePinCheck.html")
    else:
        print("Invalid")
        session.pop("atm",None)
        return redirect("/")

#//*---ACC PIN Check----------*//
@app.route("/MiniStatepinCheck", methods=["POST"])
def MiniStateenteredPin_Check():
    enter_pin = request.form["acc_pin"]

    data = session["atm"]
    user_accoun = data[11]
    x = Pin_Bal(user_accoun)
    

    # print("user given",enter_pin)
    # print("user ",x)
    if enter_pin == x:
        bal = ViewBalance(user_accoun)
        print("sucess")
        #//*----Methods to show MiniSatetement
        CurDate = datetime.today().strftime("%y-%m-%d")
        # CurDate = date.today()
        now = datetime.now()
        CurTime = now.strftime("%H:%M")
        listData = [CurDate,CurTime,user_accoun,bal]
        print("date",CurDate)
        print("time ",CurTime)
        print("balance = ",bal)
        MiniState = getFullMiniStatement(user_accoun)

        return render_template("/showminiStatement.html", userData=listData, miniS=MiniState)
    else:
        print("Invalid")
        session.pop("atm",None)
        return redirect("/")


#//*-----------MINI Statement Display------*//
@app.route("/exitMini", methods=["POST"])
def ExitMini():
        session.pop("atm",None)
        return redirect("/")



if(__name__ == "__main__"):
    app.run(debug=True)


