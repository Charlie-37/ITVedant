import json

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




#//*-------------------ATM Starting-------------------*//

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
        session["atmd"] = data
        return render_template("atmChoice.html")
    else:
        return redirect("/")


#//*---Main Starting Choice----*//
@app.route("/atmlogout")
def atmlog():
    session.pop("atmd",None)
    return redirect("/")


# //*-----First Selection-------*//
@app.route("/first_select", methods=["POST"])
def main_choi():
    firChoi = request.form["main_choice"]
    print("choice is",firChoi)
    # if firChoi == "PinChange":
    #     pass

    # elif firChoi == "MiniStatement":
    #     pass
    # elif firChoi == "Withdrawl":
    #     pass

    # elif firChoi == "BalanceEnquiry":
    #     # data = session["atm"]
    #     # bal = data[10]
    #     # bal = int(bal)
    #     return render_template("pinCheck.html")

    # elif firChoi == "GenratePin":
    #     pass

















if(__name__ == "__main__"):
    app.run(debug=True)


