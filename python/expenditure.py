from __main__ import app
import json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
db = SQLAlchemy(app)

class Expenditure_class:
    def get():
        return db.engine.execute("""
            select a.*, count(d.id) count, ifnull(sum(d.amount), 0) amount from Expenditure_class a left join (
                select b.*, count(c.id), sum(c.value) amount from Expenditure b left join Expenditure_entity c on b.id=c.expenditure_id group by(b.id)
            )d on a.id=d.class_id group by(a.id)
        """).all()
    def insert(data):
        instructuon = "insert into Expenditure_class (title) values('" + data['title'] + "')"
        db.engine.execute(text(instructuon))
    def update(id, data):
        instructuon = "update Expenditure_class set title='" + data['title'] + "' where id=" + id
        db.engine.execute(text(instructuon))
    def delete(id):
        instructuon = "delete from Expenditure_class where id=" + id
        db.engine.execute(text(instructuon))

class Expenditure:
    def get():
        instruction = "select a.*, count(b.id) count, ifnull(sum(b.value), 0) amount from Expenditure a left join Expenditure_entity b on a.id=b.Expenditure_id group by(a.id)"
        return db.engine.execute(text(instruction)).all()
    def insert(id, data):
        db.engine.execute(text("insert into Expenditure (class_id, title) values(" + id + ", '" + data['title'] + "')"))
    def update(id, data):
        db.engine.execute(text("update Expenditure set title='" + data['title'] + "', remaining=" + data['remaining'] + ", book_value=" + data['book_value'] + " where id=" + id))
    def delete(id):
        db.engine.execute(text("delete from Expenditure where id=" + id))

class Expenditure_entity:    
    def get():
        instruction = "select * from Expenditure_entity"
        return db.engine.execute(text(instruction)).all()
    def insert(id, data):
        db.engine.execute(text("insert into Expenditure_entity(expenditure_id, value, time) values("+ id + ", " + data['value'] + ", '" + data['time'] +"')"))
    def delete(id):
        db.engine.execute(text("delete from Expenditure_entity where id=" + id))