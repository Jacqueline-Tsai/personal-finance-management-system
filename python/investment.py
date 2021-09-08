from __main__ import app
import json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
db = SQLAlchemy(app)

class Investment_class:
    def get():
        return db.engine.execute("""
            select a.*, count(d.id) count, ifnull(sum(d.book_value), 0) book_value, ifnull(sum(d.realized), 0) realized from investment_class a left join (
                select b.*, count(c.id), sum(c.value) realized from investment b left join investment_entity c on b.id=c.investment_id group by(b.id)
            )d on a.id=d.class_id group by(a.id)
        """).all()
    def insert(data):
        instructuon = "insert into Investment_class (title) values('" + data['title'] + "')"
        db.engine.execute(text(instructuon))
    def update(id, data):
        instructuon = "update Investment_class set title='" + data['title'] + "' where id=" + id
        db.engine.execute(text(instructuon))
    def delete(id):
        instructuon = "delete from Investment_class where id=" + id
        db.engine.execute(text(instructuon))

class Investment:
    def get():
        instruction = "select a.*, count(b.id) count, ifnull(sum(b.value), 0) realized from investment a left join investment_entity b on a.id=b.investment_id group by(a.id)"
        return db.engine.execute(text(instruction)).all()
    def insert(id, data):
        db.engine.execute(text("insert into Investment (class_id, title, remaining, book_value) values(" + id + ", '" + data['title'] + "', " + data['remaining'] + ", " + data['book_value'] + ")"))
    def update(id, data):
        db.engine.execute(text("update Investment set title='" + data['title'] + "', remaining=" + data['remaining'] + ", book_value=" + data['book_value'] + " where id=" + id))
    def delete(id):
        db.engine.execute(text("delete from Investment where id=" + id))

class Investment_entity:    
    def get():
        return db.engine.execute(text("select * from investment_entity")).all()
    def insert(id, data):
        db.engine.execute(text("insert into Investment_entity(receipt_id, value, time) values("+ id + ", " + data['value'] + ", '" + data['date'] +"');"))
    def delete(id):
        db.engine.execute(text("delete from Investment_entity where id=" + id))