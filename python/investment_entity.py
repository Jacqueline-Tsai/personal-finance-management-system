from __main__ import app
import json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
db = SQLAlchemy(app)

class Inv_ent:
    def __init__(self):
        pass
    def insert(id, title, val, time):        
        try:
            int(val)
        except:
            return
        inst = "insert into Inv_ent (inv_id, title, value, time) values ('" + id +"', '" + title + "', " + val + ", '" + time + "')"
        db.engine.execute(text(inst))
    def update(id, title, val, time):
        try:
            int(val)
        except:
            return
        inst = "update Inv_ent set title='" + title + "', value=" + val + ", time='" + time + "' where id=" + id
        db.engine.execute(text(inst))
    def delete(id):
        inst = "delete from Inv_ent where id=" + id
        db.engine.execute(text(inst))
    def all():
        return db.engine.execute(""" 
            select id, inv_id parent_id, title, value, time from Inv_ent order by time desc;;
        """).all()
    def sum_rcpt():
        return db.engine.execute(""" 
            select ifnull(sum(value), 0) val from Inv_ent where value > 0
        """).first()['val']
    def sum_expnd():
        return -db.engine.execute(""" 
            select ifnull(sum(value), 0) val from Inv_ent where value < 0
        """).first()['val']
    def sum_mth():
        return db.engine.execute(""" 
            select year(time) as year, month(time) as month, sum(value) as val from Inv_ent group by year(time), month(time) order by year(time) ASC, month(time) ASC;
        """).all()