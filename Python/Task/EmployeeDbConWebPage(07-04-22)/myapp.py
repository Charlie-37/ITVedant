from flask import *
from DBM import *

wapp = Flask(__name__)


@wapp.route("/")

def home():
    return render_template("homepage.html")



@wapp.route("/reg")

def register():
    return render_template("addrecord.html")

@wapp.route("/emplist")

def emp_list():
    data= selectAllEmp()
    return render_template("showrecord.html" ,elist=data)

@wapp.route("/addEmp", methods=["POST"])

def add_emp():
    ids = request.form["eid"]
    name = request.form["ename"]
    contact = request.form["econtact"]
    email = request.form["Eemail"]
    passw = request.form["epass"]

    t = (ids, name, contact, email, passw)
    addEmp(t)

    return redirect("/")
    

if(__name__=="__main__"):
    wapp.run(debug=True)
