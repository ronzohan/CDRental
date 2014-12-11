from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
import datetime
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] \
    = 'postgres://postgres:Whafackles08@localhost/mygrade'
db = SQLAlchemy(app)


class CD(db.Model):
    __tablename__ = 'cd'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    rental_period = db.Column(db.Integer)
    rented = db.Column(db.String(20))

    cdrental = db.relationship("CDRentals", 
                               backref=backref('cd', uselist=False))

    def __init__(self, title, rented="No", rental_period=None):
        self.title = title
        self.rented = rented
        self.rental_period = rental_period

    def __repr__(self):
        return '<CD %r>' % self.title


class CDRentals(db.Model):
    __tablename__ = 'cdrentals'
    id = db.Column(db.Integer, primary_key=True)
    cd_id = db.Column(db.Integer, db.ForeignKey('cd.id'))
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    rental_due = db.Column(db.DateTime)

    def __init__(self, cd_id, customer_id):
        cd = CD.query.filter(CD.id == cd_id).first()

        self.cd_id = cd_id
        self.rental_due = datetime.datetime.now() + \
            datetime.timedelta(days=cd.rental_period)
        self.customer_id = customer_id

        cd.rented = 'Yes'

        db.session.add(self)
        db.session.commit()

    def print_contract(self):
        result = db.session.query(Customer.id, Customer.name,
                                  CD.id, CD.title,
                                  CDRentals.rental_due).join(CD.cdrental).first()

        return result

    def __repr__(self):
        return '<CDRentals %r>' % self.cd_id


class Customer(db.Model):
    """
    Customer Definition
    """
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    cdrental = db.relationship("CDRentals", backref=backref("customer",
                                                            uselist=False))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Customer %r>' % self.name
