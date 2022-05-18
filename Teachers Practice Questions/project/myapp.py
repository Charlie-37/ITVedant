from flask import *
from DBM import *

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/reg")
def register():
    return render_template("register.html")

@app.route("/emplist")
def emp_list():
    data = selectAllEmp()
    return render_template("emplist.html", elist=data)

@app.route("/addEmp", methods=["POST"])
def add_emp():
    ids = request.form["id"]
    name = request.form["name"]
    contact = request.form["contact"]
    email = request.form["email"]
    passw = request.form["passw"]

    t = (ids, name, contact, email, passw)
    addEmp(t)
    return redirect("/")

    

if(__name__=="__main__"):
    app.run(debug=True)
