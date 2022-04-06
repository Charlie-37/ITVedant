
from flask import * # Flask, render_template, redirect, request

wapp = Flask(__name__)

##@wapp.route("/")
##@wapp.route("/home")
##
##def home():
##    return "<h1>This is Home Page</h1>"
##
##@wapp.route("/aboutus")
##
##def page2():
##    return "<h1>This is Second Page</h1>"
##
##if(__name__=="__main__"):
##    wapp.run(debug=True)



@wapp.route("/")
@wapp.route("/home")

def home():
    return render_template("pageHome.html")

@wapp.route("/<name>")

def page3(name):
    var = name
    return render_template("page3.html",data=name)

if(__name__=="__main__"):
    wapp.run(debug=True)
