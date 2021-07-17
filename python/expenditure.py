from __main__ import app
import json
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

class Expnd:
    def __init__(self):
        pass
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