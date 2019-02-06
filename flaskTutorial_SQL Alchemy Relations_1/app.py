from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate

app = Flask(__name__)

baseDir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(baseDir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app, db)
################################################################################################
#models

class Department(db.Model):
    __tablename__ = 'Department'

    department_id = db.Column(db.Integer, primary_key = True)
    department_name = db.Column(db.Text)

    def __init__(self, department_name):
        self.department_name = department_name

    def __repr__(self):
        return f'department_id : {self.department_id}, department_name : {self.department_name}'
#--------------------------------------------------------------------------------------------------
class EmployeeData(db.Model):
    __tablename__ = 'EmployeeData'

    employee_id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    department = db.relationship('Department', backref = 'EmployeeData')
    department_id = db.Column(db.Integer, db.ForeignKey('Department.department_id'))

    def __init__(self, first_name, last_name, department_id):
        self.first_name = first_name
        self.last_name = last_name
        self.department_id = department_id

    def __repr__(self):
        return f'name : {self.first_name} {self.last_name}, department_id : {self.department_id}, department_name : {self.department.department_name}'
