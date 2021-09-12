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
            select sum(value) value from receipt_entity;
        """).first()['value'] + db.engine.execute("""
            select sum(value) value from expenditure_entity;
        """).first()['value'] + db.engine.execute("""
            select sum(value) value from investment_entity;
        """).first()['value'])
    def balance():
        value_list = Dashboard.asset_allocation()['value']
        return int(sum(value_list) - db.engine.execute("""
            select sum(value) value from receipt_entity where time>(select now());
        """).first()['value'] + db.engine.execute("""
            select sum(value) value from expenditure_entity where time>(select now());
        """).first()['value'])
    def receipt_sum():
        return int(db.engine.execute(""" 
            select ifnull(sum(value), 0) value from receipt_entity 
        """).first()['value'])
    def receipt_max_month():
        legacyrow = db.engine.execute(""" 
            select year, month, value from (
                select year(time) year, month(time) month, sum(value) value from receipt_entity group by year(time), month(time)
            ) receipt_grouped where value = (
                select max(value) from (
                    select year(time) year, month(time) month, sum(value) value from receipt_entity group by year(time), month(time)
                ) receipt_grouped
            )
        """).first()
        return {'year': legacyrow['year'], 'month': legacyrow['month'], 'value': int(legacyrow['value'])}
    def receipt_max_year():
        legacyrow = db.engine.execute(""" 
            select year, value from (
                select year(time) year, sum(value) value from receipt_entity group by year(time)
            ) receipt_grouped where value = (
                select max(value) from (
                    select year(time) year, sum(value) value from receipt_entity group by year(time)
                ) receipt_grouped
            )
        """).first()
        return {'year': legacyrow['year'], 'value': int(legacyrow['value'])}
    def expenditure_sum():
        return -int(db.engine.execute(""" 
            select ifnull(sum(value), 0) value from expenditure_entity 
        """).first()['value'])
    def expenditure_max_month():
        legacyrow = db.engine.execute(""" 
            select year, month, value from (
                select year(time) year, month(time) month, sum(value) value from expenditure_entity group by year(time), month(time)
            ) expenditure_grouped where value = (
                select max(value) from (
                    select year(time) year, month(time) month, sum(value) value from expenditure_entity group by year(time), month(time)
                ) expenditure_grouped
            )
        """).first()
        return {'year': legacyrow['year'], 'month': legacyrow['month'], 'value': -int(legacyrow['value'])}
    def expenditure_max_year():
        legacyrow = db.engine.execute(""" 
            select year, value from (
                select year(time) year, sum(value) value from expenditure_entity group by year(time)
            ) expenditure_grouped where value = (
                select max(value) from (
                    select year(time) year, sum(value) value from expenditure_entity group by year(time)
                ) expenditure_grouped
            )
        """).first()    
        return {'year': legacyrow['year'], 'value': -int(legacyrow['value'])}
    def investment_sum():
        return Dashboard.investment_receipt_sum()-Dashboard.investment_expenditure_sum()
    def investment_receipt_sum():
        return int(db.engine.execute(""" 
            select ifnull(sum(value), 0) value from investment_entity where value>0
        """).first()['value'])
    def investment_expenditure_sum():
        return -int(db.engine.execute(""" 
            select ifnull(sum(value), 0) value from investment_entity where value<0
        """).first()['value'])
    def investment_best():
        legacyrow = db.engine.execute("""
            select title, roi from (
                select a.id, a.title, ifnull(-(a.book_value + sum(b.value))/sum(b.value), 0) roi from investment a left join investment_entity b on a.id=b.investment_id group by(a.id)
            ) investment_grouped where roi = (
                select max(roi) from (
                    select a.id, ifnull(-(a.book_value + sum(b.value))/sum(b.value), 0) roi from investment a left join investment_entity b on a.id=b.investment_id group by(a.id)
                ) investment_grouped
            )
        """).first()
        return {'title': legacyrow['title'], 'roi':float(legacyrow['roi'])}
    def investment_worst():
        legacyrow = db.engine.execute("""
            select title, roi from (
                select a.id, a.title, ifnull(-(a.book_value + sum(b.value))/sum(b.value), 0) roi from investment a left join investment_entity b on a.id=b.investment_id group by(a.id)
            ) investment_grouped where roi = (
                select min(roi) from (
                    select a.id, ifnull(-(a.book_value + sum(b.value))/sum(b.value), 0) roi from investment a left join investment_entity b on a.id=b.investment_id group by(a.id)
                ) investment_grouped
            )
        """).first()
        return {'title': legacyrow['title'], 'roi':float(legacyrow['roi'])}