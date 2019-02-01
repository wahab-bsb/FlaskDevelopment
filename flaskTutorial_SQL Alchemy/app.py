import os
from flask import Flask, redirect, url_for, session, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

baseDir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(baseDir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# models for database
####################################################################

class CustomerData(db.Model):
    __tablename__ = 'CustomerData'

    id = db.Column(db.Integer, primary_key = True)
    firstName = db.Column(db.Text)
    lastName = db.Column(db.Text)
    age = db.Column(db.Integer)

    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

    def __repr__(self):
        return 'name : ' + self.firstName + ' ' + self.lastName + ', Age : ' + str(self.age)

####################################################################
