from flask import Flask,render_template,request
import concept
import itertools
import string

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/analyze",methods=['GET','POST'])
def analyze():
    if request.method == 'POST':
        fip = request.form['First_Input']
        sip = request.form['Second_Input']
        etoip = request.form['IsEqual1']
        ser=request.form['service']
        if ser=='Addition':
            ans1,ans2=concept.solve(fip+' + '+sip+' = ' + etoip)
        else:
            ans1,ans2=concept.solve(fip+' - '+sip+' = ' + etoip)
        return render_template('index.html',answer=ans1,answers=ans2,  FIP=fip,SIP=sip,et=etoip)

app.run(debug=True)