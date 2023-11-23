from . import db

class Employee(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50))
    profession = db.Column(db.strion(50))







"""
CREATE TABLE IF NOT EXISTS employee(
    id int primarykey,
    name string,
    profession string
)"""