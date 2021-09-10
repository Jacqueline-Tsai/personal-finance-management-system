from __main__ import app
import json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
db = SQLAlchemy(app)

class Dashboard:
    def asset_allocation():
        data_list = db.engine.execute("""
            select title, book_value value from investment;
        """).mappings().all() + [{ 'title': 'cash', 'value': Dashboard.cash()}]
        return {'title': [data['title'] for data in data_list], 'value': [data['value'] for data in data_list]}
    def cash():
        return int(db.engine.execute("""
            select sum(value) val from receipt_entity;
        """).first()['val'] + db.engine.execute("""
            select sum(value) val from expenditure_entity;
        """).first()['val'] + db.engine.execute("""
            select sum(value) val from investment_entity;
        """).first()['val'])
    def balance():
        value_list = Dashboard.asset_allocation()['value']
        return sum(value_list)
    def receipt_sum():
        return db.engine.execute(""" 
            select ifnull(sum(value), 0) value from receipt_entity 
        """).first()['value']
    def expenditure_sum():
        return db.engine.execute(""" 
            select ifnull(sum(value), 0) value from expenditure_entity 
        """).first()['value']
