from __main__ import app
import json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
db = SQLAlchemy(app)

class Receipt_class:
    def get():
        return db.engine.execute("""
            select a.*, count(d.id) count, ifnull(sum(d.amount), 0) amount from Receipt_class a left join (
                select b.*, count(c.id), sum(c.value) amount from Receipt b left join Receipt_entity c on b.id=c.receipt_id group by(b.id)
            )d on a.id=d.class_id group by(a.id)
        """).all()
    def insert(data):
        instructuon = "insert into Receipt_class (title) values('" + data['title'] + "')"
        db.engine.execute(text(instructuon))
    def update(id, data):
        instructuon = "update Receipt_class set title='" + data['title'] + "' where id=" + id
        db.engine.execute(text(instructuon))
    def delete(id):
        instructuon = "delete from Receipt_class where id=" + id
        db.engine.execute(text(instructuon))

class Receipt:
    def get():
        instruction = "select a.*, count(b.id) count, ifnull(sum(b.value), 0) amount from Receipt a left join Receipt_entity b on a.id=b.Receipt_id group by(a.id)"
        return db.engine.execute(text(instruction)).all()
    def insert(id, data):
        db.engine.execute(text("insert into Receipt (class_id, title) values(" + id + ", '" + data['title'] + "')"))
    def update(id, data):
        db.engine.execute(text("update Receipt set title='" + data['title'] + "', remaining=" + data['remaining'] + ", book_value=" + data['book_value'] + " where id=" + id))
    def delete(id):
        db.engine.execute(text("delete from Receipt where id=" + id))

class Receipt_entity:    
    def get():
        instruction = "select * from Receipt_entity"
        return db.engine.execute(text(instruction)).all()
    def insert(id, data):
        db.engine.execute(text("insert into Receipt_entity(receipt_id, value, time) values("+ id + ", " + data['value'] + ", '" + data['time'] +"')"))
    def delete(id):
        db.engine.execute(text("delete from Receipt_entity where id=" + id))