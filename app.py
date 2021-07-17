from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
from python.receipt import Rcpt
from python.receipt_entity import Rcpt_ent
from  python.expenditure import Expnd
#from  python.expenditure_entity import Expnd_ent
from  python.investment import Inv
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:jaychou0118@127.0.0.1:3306/Finance"
db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("index.html")

# dashboard
@app.route("/dashboard", methods=['GET'])
def dashboard():
    data = {'rcpt_sum': Rcpt_ent.sum(), 'expnd_sum': Expnd.sum(), 'inv_rcpt_sum': Inv.sum_rcpt(), 'inv_expnd_sum': Inv.sum_expnd(),
    'inv_sum': Inv.sum_rcpt()-Inv.sum_expnd(), 'balance': Rcpt_ent.sum()+Inv.sum_rcpt()-Expnd.sum()-Inv.sum_expnd(), 
    'rcpt_max_mth': Rcpt_ent.max_mth(), 'expnd_max_mth': Expnd.max_mth(), 'rcpt_max_yr': Rcpt_ent.max_yr() , 'expnd_max_yr': Expnd.max_yr()}
    return render_template("dashboard.html", data=data)

# receipt
@app.route("/receipt", methods=['GET'])
def rcpt():
    data = {'all': Rcpt.all(), 'ent': Rcpt_ent.all()}
    return render_template("receipt.html", data=data)

@app.route("/receipt/post", methods=['POST'])
def rcpt_post():
    Rcpt.insert(request.values)
    return redirect('http://127.0.0.1:5000/receipt')

@app.route("/receipt/put/<id>", methods=['POST'])
def rcpt_put(id):
    Rcpt.update(id, request.values)
    return redirect('http://127.0.0.1:5000/receipt')

@app.route("/receipt/delete/<id>", methods=['POST'])
def rcpt_delete(id):
    Rcpt.delete(id)
    return redirect('http://127.0.0.1:5000/receipt')

@app.route("/receipt/ent/post/<id>", methods=['POST'])
def rcpt_ent_post(id):
    Rcpt_ent.insert(id, request.values['title'], request.values['value'], request.values['time'])
    return redirect('http://127.0.0.1:5000/receipt')

@app.route("/receipt/ent/put/<id>", methods=['POST'])
def rcpt_ent_put(id):
    Rcpt_ent.update(id, request.values['title'], request.values['value'], request.values['time'])
    return redirect('http://127.0.0.1:5000/receipt')

@app.route("/receipt/ent/delete/<id>", methods=['POST'])
def rcpt_ent_delete(id):
    Rcpt_ent.delete(id)
    return redirect('http://127.0.0.1:5000/receipt')

# expenditure
"""@app.route("/expenditure", methods=['GET'])
def Expnd():
    data = {'all': Expnd.all(), 'ent': Expnd.ent()}
    return render_template("expenditure.html", data=data)

@app.route("/expenditure/post", methods=['POST'])
def expnd_post():
    Expnd.insert(request.values)
    return redirect('http://127.0.0.1:5000/expenditure')

@app.route("/expenditure/put/<id>", methods=['POST'])
def expnd_put(id):
    Expnd.update(id, request.values)
    return redirect('http://127.0.0.1:5000/expenditure')

@app.route("/expenditure/delete/<id>", methods=['POST'])
def expnd_delete(id):
    Expnd.delete(id)
    return redirect('http://127.0.0.1:5000/expenditure')

@app.route("/expenditure/ent/post/<id>", methods=['POST'])
def expnd_ent_post(id):
    Expnd_ent.insert(id, request.values['title'], request.values['value'], request.values['time'])
    return redirect('http://127.0.0.1:5000/expenditure')

@app.route("/expenditure/ent/put/<id>", methods=['POST'])
def expnd_ent_put(id):
    Expnd_ent.update(id, request.values['title'], request.values['value'], request.values['time'])
    return redirect('http://127.0.0.1:5000/expenditure')

@app.route("/expenditure/ent/delete/<id>", methods=['POST'])
def expnd_ent_delete(id):
    Expnd_ent.delete(id)
    return redirect('http://127.0.0.1:5000/expenditure')
"""
# investment
@app.route("/investment", methods=['GET'])
def inv():
    data = {'all': Inv.all(), 'ent': Inv.ent()}
    return render_template("investment.html", data=data)

@app.route("/investment/post", methods=['POST'])
def inv_post():
    Inv.insert(request.values)
    return redirect('http://127.0.0.1:5000/investment')

@app.route("/investment/put/<id>", methods=['POST'])
def inv_put(id):
    Inv.update(id, request.values)
    return redirect('http://127.0.0.1:5000/investment')

@app.route("/investment/delete/<id>", methods=['POST'])
def inv_delete(id):
    Inv.delete(id)
    return redirect('http://127.0.0.1:5000/investment')

@app.route("/investment/ent/post/<id>", methods=['POST'])
def inv_ent_post(id):
    Inv_ent.insert(id, request.values['title'], request.values['value'], request.values['time'])
    return redirect('http://127.0.0.1:5000/investment')

@app.route("/investment/ent/put/<id>", methods=['POST'])
def inv_ent_put(id):
    Inv_ent.update(id, request.values['title'], request.values['value'], request.values['time'])
    return redirect('http://127.0.0.1:5000/investment')

@app.route("/investment/ent/delete/<id>", methods=['POST'])
def inv_ent_delete(id):
    Inv_ent.delete(id)
    return redirect('http://127.0.0.1:5000/investment')

# expenditure




app.run(debug=True)