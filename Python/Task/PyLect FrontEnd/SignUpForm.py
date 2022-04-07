
from flask import *

wapp = Flask(__name__)

@wapp.route("/")
@wapp.route("/home")

def home():
    return'''<h1>Welcome to Sign Up Form </h1><br>

                <h2><a href="signup">SignUp</a></h2>'''

@wapp.route("/signup")

def SignUp():
    return render_template("form1.html")

if(__name__=="__main__"):
    wapp.run(debug=True)

