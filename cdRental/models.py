from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from sqlalchemy.sql.schema import ForeignKey

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:Whafackles08@localhost/mygrade'
db = SQLAlchemy(app)


class CD(db.Model):
    __tablename__ = 'cd'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    rental_period = db.Column(db.Integer)
    rented = db.Column(db.String(20))

    def __init__(self, title, rented="No", rental_period=None):
        self.title = title
        self.rented = rented
        self.rental_period = rental_period

    def __repr__(self):
        return '<CD %r>' % self.title


class CDRentals(db.Model):
    __tablename__ = 'cdrentals'
    id = db.Column(db.Integer, primary_key=True)
    cd_id = db.Column(db.Integer, ForeignKey('cd.id'))
    customer_id = db.Column(db.Integer, ForeignKey('customer.id'))
    rental_due = db.Column(db.DateTime)

    cd = db.relationship("CD", backref=backref("CDRentals", uselist=False))
    customer = db.relationship("Customer", backref=backref("CDRentals",
                                                           uselist=False))

    def __init__(self, cd, customer, rental_due):
        self.cd = cd
        self.rental_due = rental_due
        self.customer = customer

    def __repr__(self):
        return '<CDRentals %r %r>' % self.cd_id, self.rental_due


class Customer(db.Model):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Customer %r>' % self.name
