from flask import Flask, render_template, jsonify
import json
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:jaychou0118@127.0.0.1:3306/Finance"
db = SQLAlchemy(app)

def sum_rcpt():
    return db.engine.execute(""" 
        select ifnull(sum(value), 0) val from Rcpt_ent 
    """).first()['val']

def sum_expnd():
    return db.engine.execute(""" 
        select ifnull(sum(value), 0) val from Expnd_ent
    """).first()['val']

def sum_inv_rcpt():
    return db.engine.execute(""" 
        select ifnull(sum(value), 0) val from Inv_ent where value > 0
    """).first()['val']

def sum_inv_expnd():
    return -db.engine.execute(""" 
        select ifnull(sum(value), 0) val from Inv_ent where value < 0
    """).first()['val']

def mth_rcpt():
    return db.engine.execute(""" 
        select ifnull(max(val), 0) val from (
            select time, sum(value) val from Rcpt_ent group by time
        ) as t;
    """).first()['val']
    
def mth_expnd():
    return db.engine.execute(""" 
        select ifnull(max(val), 0) val from (
            select time, sum(value) val from Expnd_ent group by time
        ) as t;
    """).first()['val']

def yr_rcpt():
    return db.engine.execute(""" 
        select ifnull(max(val), 0) val from (
            select year(time), sum(value) as val from Rcpt_ent group by year(time)
        ) as t;
    """).first()['val']
    
def yr_expnd():
    return db.engine.execute(""" 
        select ifnull(max(val), 0) val from (
            select year(time), sum(value) as val from Expnd_ent group by year(time)
        ) as t;
    """).first()['val']

def rcpt():
    return db.engine.execute(""" 
        select * from Rcpt r1 join (
            select rcpt_id, min(time) min, max(time) max, count(id) count, sum(value) sum from Rcpt_ent group by rcpt_id
        ) as r2 on r1.id=r2.rcpt_id;
    """).all()

def rcpt_ent():
    return db.engine.execute(""" 
        select * from Rcpt_ent;
    """).all()

def time_rcpt():
    return db.engine.execute(""" 
        select year(time) as y, month(time) as m, sum(value) as val from Rcpt_ent group by year(time), month(time), month(time) order by year(time) ASC, month(time) ASC;
    """).all()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", rcpt=sum_rcpt(), expnd=sum_expnd(), inv_rcpt=sum_inv_rcpt(), inv_expnd=sum_inv_expnd(), inv=sum_inv_rcpt()-sum_inv_expnd(), balance=sum_rcpt()+sum_inv_rcpt()-sum_expnd()-sum_inv_expnd(), mth_rcpt=mth_rcpt(), mth_expnd=mth_expnd(), yr_rcpt=yr_rcpt(), yr_expnd=yr_expnd())

@app.route("/reciept")
def reciept():
    return render_template("reciept.html", rcpt=rcpt(), ent=rcpt_ent(), time=json.dumps([[t['y'], t['m'], int(t['val'])] for t in time_rcpt()]))

@app.route("/expenditure")
def expenditure():
    return render_template("expenditure.html")

@app.route("/investment")
def investment():
    return render_template("investment.html")

app.run()