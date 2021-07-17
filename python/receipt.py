from __main__ import app
import json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
db = SQLAlchemy(app)

class Rcpt:
    def __init__(self):
        pass
    def all():
        return db.engine.execute(""" 
            select * from Rcpt r1 left join (
                select rcpt_id, min(time) min_t, max(time) max_t, count(id) cnt, sum(value) sum from Rcpt_ent group by rcpt_id
            ) as r2 on r1.id=r2.rcpt_id order by r2.max_t desc;
        """).all()
    def insert(val):
        inst = "insert into Rcpt (user_acc, title) values ('jaynnah01180118@gmail.com', '" + val['title'] + "')"
        db.engine.execute(text(inst))
    def update(id, val):
        inst = "update Rcpt set title='" + val['title'] + "' where id=" + id + " and user_acc='jaynnah01180118@gmail.com'"
        db.engine.execute(text(inst))
    def delete(id):
        inst = "delete from Rcpt where id=" + id + " and user_acc='jaynnah01180118@gmail.com'"
        db.engine.execute(text(inst))