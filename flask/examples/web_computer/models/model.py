from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Employee(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    fname = db.Column(db.String(50))
    lname = db.Column(db.strion(50))
    age = db.Column(db.strion(50))
    city = db.Column(db.strion(50))