from __main__ import app
import json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
db = SQLAlchemy(app)

class Expnd_ent:
    def __init__(self):
        pass
    def insert(id, title, val, time):        
        try:
            int(val)
        except:
            return
        inst = "insert into Expnd_ent (expnd_id, title, value, time) values ('" + id +"', '" + title + "', " + val + ", '" + time + "')"
        db.engine.execute(text(inst))
    def update(id, title, val, time):
        try:
            int(val)
        except:
            return
        inst = "update Expnd_ent set title='" + title + "', value=" + val + ", time='" + time + "' where id=" + id
        db.engine.execute(text(inst))
    def delete(id):
        inst = "delete from Expnd_ent where id=" + id
        db.engine.execute(text(inst))
    def all():
        return db.engine.execute(""" 
            select id, expnd_id parent_id, title, value, time from Expnd_ent order by time desc;
        """).all()
    def sum():
        return db.engine.execute(""" 
            select ifnull(sum(value), 0) val from Expnd_ent 
        """).first()['val']
    def max_mth():
        return db.engine.execute(""" 
            select ifnull(max(val), 0) val from (
                select time, sum(value) val from Expnd_ent group by time
            ) as t;
        """).first()['val']
    def max_yr():
        return db.engine.execute(""" 
            select ifnull(max(val), 0) val from (
                select year(time), sum(value) as val from Expnd_ent group by year(time)
            ) as t;
        """).first()['val']
    def sum_mth():
        return db.engine.execute(""" 
            select year(time) as year, month(time) as month, sum(value) as val from Expnd_ent group by year(time), month(time) order by year(time) ASC, month(time) ASC;
        """).all()
        return