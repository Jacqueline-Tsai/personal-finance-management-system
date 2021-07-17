from __main__ import app
import json
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

class Inv:
    def __init__(self):
        pass
    def all():
        #return db.engine.execute(""" 
        #    select i1.id, i1.title, min_t, max_t, ifnull(i3.sum, 0) rcpt_sum, ifnull(i3.cnt, 0) rcpt_cnt, ifnull(i4.sum, 0) expnd_sum, ifnull(i4.cnt, 0) expnd_cnt
        #    from Inv i1 left join (
        #        select inv_id id, min(time) min_t, max(time) max_t from Inv_ent group by inv_id
        #    ) as i2 on i1.id=i2.id left join (
        #        select inv_id id, count(id) cnt, sum(value) sum from Inv_ent where value>0 group by inv_id
        #    ) as i3 on i1.id=i3.id left join (
        #        select inv_id id, count(id) cnt, -sum(value) sum from Inv_ent where value<0 group by inv_id
        #    ) as i4 on i1.id=i4.id;
        #""").all()
        return db.engine.execute("""
            select * from Inv i1 left join (
                select inv_id, min(time) min_t, max(time) max_t, count(id) cnt, sum(value) sum from Inv_ent group by inv_id
            ) as i2 on i1.id=i2.inv_id order by i2.max_t desc;
        """).all()
    def ent():
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
    