from flask import *

f=Flask(__name__)

@f.route("/")
def home():
    return "<h1>Flask Based API</h1>"

@f.route("/check/<int:no>")
def check_no(no):
    d={}
    if no%2==0:
        d["Number"]=no
        d["status"]=True
        d["description"]="This is Even NUmber"
    else:
        d["Number"]=no
        d["status"]=False
        d["description"]="This is Odd NUmber"
    return jsonify(d)



if __name__=='__main__':
    f.run(debug=True)
