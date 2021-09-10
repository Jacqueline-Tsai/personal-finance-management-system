from datetime import date
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
from python.receipt import Receipt_class
from python.receipt import Receipt
from python.receipt import Receipt_entity
from python.expenditure import Expenditure_class
from python.expenditure import Expenditure
from python.expenditure import Expenditure_entity
from python.investment import Investment_class
from python.investment import Investment
from python.investment import Investment_entity
from python.dashboard import Dashboard
import json

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:jaychou0118@127.0.0.1:3306/Finance"
db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("index.html")

# dashboard
@app.route("/dashboard", methods=['GET'])
def dashboard():
    data = {'asset_allocation': Dashboard.asset_allocation(), 'balance': Dashboard.balance()}
    #print(type(json.dumps(data, indent = 4)), data)
    #data = {'Receipt_sum': Receipt_ent.sum(), 'Expenditure_sum': Expenditure_ent.sum(), 'inv_Receipt_sum': Inv_ent.sum_Receipt(), 'inv_Expenditure_sum': Inv_ent.sum_Expenditure(),
    #'inv_sum': Inv_ent.sum_Receipt()-Inv_ent.sum_Expenditure(), 'balance': Receipt_ent.sum()+Inv_ent.sum_Receipt()-Expenditure_ent.sum()-Inv_ent.sum_Expenditure(), 
    #'Receipt_max_mth': Receipt_ent.max_mth(), 'Expenditure_max_mth': Expenditure_ent.max_mth(), 'Receipt_max_yr': Receipt_ent.max_yr() , 'Expenditure_max_yr': Expenditure_ent.max_yr()}
    return render_template("dashboard.html", data=json.dumps(data, indent = 4))

# receipt
@app.route("/receipt", methods=['GET'])
def receipt():
    data = {'receipt_class': Receipt_class.get(), 'receipt': Receipt.get(), 'receipt_entity': Receipt_entity.get()}
    return render_template("receipt.html", data=data)

@app.route("/post/receipt_class", methods=['POST'])
def post_receipt_class():
    Receipt_class.insert(request.values)
    return redirect('http://127.0.0.1:5000/receipt')

@app.route("/put/receipt_class/<id>", methods=['POST'])
def put_receipt_class(id):
    Receipt_class.update(id, request.values)
    return redirect('http://127.0.0.1:5000/receipt')

@app.route("/delete/receipt_class/<id>", methods=['POST'])
def delete_receipt_class(id):
    Receipt_class.delete(id)
    return redirect('http://127.0.0.1:5000/receipt')

@app.route("/post/receipt/<id>", methods=['POST'])
def post_receipt(id):
    Receipt.insert(id, request.values)
    return redirect('http://127.0.0.1:5000/receipt')

@app.route("/put/receipt/<id>", methods=['POST'])
def put_receipt(id):
    Receipt.update(id, request.values)
    return redirect('http://127.0.0.1:5000/receipt')

@app.route("/delete/receipt/<id>", methods=['POST'])
def delete_receipt(id):
    Receipt.delete(id)
    return redirect('http://127.0.0.1:5000/receipt')

@app.route("/post/receipt_entity/<id>", methods=['POST'])
def post_receipt_entity(id):
    Receipt_entity.insert(id, request.values)
    return redirect('http://127.0.0.1:5000/receipt')

@app.route("/delete/receipt_entity/<id>", methods=['POST'])
def delete_receipt_entity(id):
    Receipt_entity.delete(id)
    return redirect('http://127.0.0.1:5000/receipt')

# expenditure
@app.route("/expenditure", methods=['GET'])
def expenditure():
    data = {'expenditure_class': Expenditure_class.get(), 'expenditure': Expenditure.get(), 'expenditure_entity': Expenditure_entity.get()}
    return render_template("expenditure.html", data=data)

@app.route("/post/expenditure_class", methods=['POST'])
def post_expenditure_class():
    Expenditure_class.insert(request.values)
    return redirect('http://127.0.0.1:5000/expenditure')

@app.route("/put/expenditure_class/<id>", methods=['POST'])
def put_expenditure_class(id):
    Expenditure_class.update(id, request.values)
    return redirect('http://127.0.0.1:5000/expenditure')

@app.route("/delete/expenditure_class/<id>", methods=['POST'])
def delete_expenditure_class(id):
    Expenditure_class.delete(id)
    return redirect('http://127.0.0.1:5000/expenditure')

@app.route("/post/expenditure//<id>", methods=['POST'])
def post_expenditure(id):
    Expenditure.insert(id, request.values)
    return redirect('http://127.0.0.1:5000/expenditure')

@app.route("/put/expenditure/<id>", methods=['POST'])
def put_expenditure(id):
    Expenditure.update(id, request.values)
    return redirect('http://127.0.0.1:5000/expenditure')

@app.route("/delete/expenditure/<id>", methods=['POST'])
def delete_expenditure(id):
    Expenditure.delete(id)
    return redirect('http://127.0.0.1:5000/expenditure')

@app.route("/post/expenditure_entity/<id>", methods=['POST'])
def post_expenditure_entity(id):
    Expenditure_entity.insert(id, request.values)
    return redirect('http://127.0.0.1:5000/expenditure')

@app.route("/delete/expenditure_entity/<id>", methods=['POST'])
def delete_expenditure_entity(id):
    Expenditure_entity.delete(id)
    return redirect('http://127.0.0.1:5000/expenditure')

# investment
@app.route("/investment", methods=['GET'])
def investment():
    data = {'investment_class': Investment_class.get(), 'investment': Investment.get(), 'investment_entity': Investment_entity.get()}
    return render_template("investment.html", data=data)

@app.route("/post/investment_class", methods=['POST'])
def post_investment_class():
    #print(request.values['title'])
    Investment_class.insert(request.values)
    return redirect('http://127.0.0.1:5000/investment')

@app.route("/put/investment_class/<id>", methods=['POST'])
def put_investment_class(id):
    #print(request.values['title'])
    Investment_class.update(id, request.values)
    return redirect('http://127.0.0.1:5000/investment')

@app.route("/delete/investment_class/<id>", methods=['POST'])
def delete_investment_class(id):
    Investment_class.delete(id)
    return redirect('http://127.0.0.1:5000/investment')

@app.route("/post/investment/<id>", methods=['POST'])
def post_investment(id):
    Investment.insert(id, request.values)
    return redirect('http://127.0.0.1:5000/investment')

@app.route("/put/investment/<id>", methods=['POST'])
def put_investment(id):
    Investment.update(id, request.values)
    return redirect('http://127.0.0.1:5000/investment')

@app.route("/delete/investment/<id>", methods=['POST'])
def delete_investment(id):
    Investment.delete(id)
    return redirect('http://127.0.0.1:5000/investment')

@app.route("/post/investment_entity/<id>", methods=['POST'])
def post_investment_entity(id):
    Investment_entity.insert(id, request.values)
    return redirect('http://127.0.0.1:5000/investment')

@app.route("/delete/investment_entity/<id>", methods=['POST'])
def delete_investment_entity(id):
    Investment_entity.delete(id)
    return redirect('http://127.0.0.1:5000/investment')

# receipt anaysis
@app.route("/receipt/anaysis", methods=['GET'])
def receipt_anaysis():
    today = date.today()
    min_year, max_year, min_month, max_month = today.year, today.year, today.month, today.month

    Receipt_sum_mth, Expenditure_sum_mth, inv_sum_mth = Receipt_ent.sum_mth(), Expenditure_ent.sum_mth(), Inv_ent.sum_mth()
    time, Receipt, Expenditure, inv = [], [], [], []
    Receipt_idx, Expenditure_idx, inv_idx = 0, 0, 0
    

    if len(Receipt_sum_mth) > 0 and (Receipt_sum_mth[0][0] < min_year or (Receipt_sum_mth[0][0] == min_year and Receipt_sum_mth[0][1] < min_month)):
        min_year, min_month = Receipt_sum_mth[0][0], Receipt_sum_mth[0][1]
    if len(Expenditure_sum_mth) > 0 and (Expenditure_sum_mth[0][0] < min_year or (Expenditure_sum_mth[0][0] == min_year and Expenditure_sum_mth[0][1] < min_month)):
        min_year, min_month = Expenditure_sum_mth[0][0], Expenditure_sum_mth[0][1]
    if len(inv_sum_mth) > 0 and (inv_sum_mth[0][0] < min_year or (inv_sum_mth[0][0] == min_year and inv_sum_mth[0][1] < min_month)):
        min_year, min_month = inv_sum_mth[0][0], inv_sum_mth[0][1]

    while min_year < max_year or (min_year == max_year and min_month <= max_month):
        if Receipt_idx < len(Receipt_sum_mth) and Receipt_sum_mth[Receipt_idx][0] == min_year and Receipt_sum_mth[Receipt_idx][1] == min_month:
            Receipt += [int(str(Receipt_sum_mth[Receipt_idx][2]))]
            Receipt_idx += 1
        else:
            Receipt += [0]

        if Expenditure_idx < len(Expenditure_sum_mth) and Expenditure_sum_mth[Expenditure_idx][0] == min_year and Expenditure_sum_mth[Expenditure_idx][1] == min_month:
            Expenditure += [Expenditure_sum_mth[Expenditure_idx][2]]
            Expenditure_idx += 1
        else:
            Expenditure += [0]

        if inv_idx < len(inv_sum_mth) and inv_sum_mth[inv_idx][0] == min_year and inv_sum_mth[inv_idx][1] == min_month:
            inv += [int(str(inv_sum_mth[inv_idx][2]))]
            inv_idx += 1
        else:
            inv += [0]

        time += [str(min_year)+'-'+str(min_month)]
        min_month += 1
        if min_month == 13:
            min_month = 1
            min_year += 1
    
    data = {'time': time, 'Receipt': Receipt, 'Expenditure': Expenditure, 'inv': inv}
    return render_template('receipt_analysis.html', data=data)

app.run(debug=True)