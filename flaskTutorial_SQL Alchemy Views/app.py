from flask import Flask, render_template, url_for, redirect, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import AddEmployee, DeleteEmployee, SearchEmployee
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'

baseDir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(baseDir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
#with app.app_context():
from models import *

Migrate(app, db)

###########################################################################################
############################### Routes ####################################################
###########################################################################################

@app.route('/')
def index():
    return render_template('index.html')

#------------------------------------------------------------------------------------------

@app.route('/AddEmployee', methods = ['GET', 'POST'])
def addEmployee():
    addForm = AddEmployee()

    if addForm.validate_on_submit():
        record = Employee(addForm.first_name.data, addForm.last_name.data, addForm.dob.data, addForm.cnic.data, addForm.qualification.data, addForm.department.data)
        db.session.add_all([record])
        db.session.commit()
        session['id'] = record.employee_id
        session['first_name'] = addForm.first_name.data
        session['last_name'] = addForm.last_name.data
        session['cnic'] = addForm.cnic.data
        session['dob'] = addForm.dob.data
        session['qualification'] = addForm.qualification.data
        session['department'] = addForm.department.data
        return redirect(url_for('recordEntered'))
    return render_template('addEmployeeDetails.html', addForm = addForm)

#-------------------------------------------------------------------------------------------
@app.route('/recordEntered')
def recordEntered():
    return render_template('recordEntered.html')

#-------------------------------------------------------------------------------------------
@app.route('/viewAllRecords')
def viewAllRecords():
    records = Employee.query.all()
    return render_template('viewAllRecords.html', records = records)

#-------------------------------------------------------------------------------------------
@app.route('/ViewRecord', methods = ['POST', 'GET'])
def ViewRecord():
    form = SearchEmployee()
    if form.validate_on_submit():
        record = Employee.query.get(form.employeeId.data)
        return render_template('searchDetails.html', record = record)
    return render_template('searchRecord.html', form = form)

#-------------------------------------------------------------------------------------------
@app.route('/update', methods = ['GET', 'POST'])
def update():
    form = SearchEmployee()
    if form.validate_on_submit():
        record = Employee.query.get(form.employeeId.data)
        if record:
            id = form.employeeId.data
            return redirect(url_for('updateEmployeeRecord', id = id))
        else:
            return '<p> Record doesnot exist </p>'
    return render_template('update.html', form = form)

#-------------------------------------------------------------------------------------------
@app.route('/updateEmployeeRecord/<id>', methods = ['GET', 'POST'])
def updateEmployeeRecord(id):
    record = Employee.query.get(id)
    form = AddEmployee()
    if form.validate_on_submit():
        record = Employee.query.get(id)
        record.first_name = form.first_name.data
        record.last_name = form.last_name.data
        record.dob = form.dob.data
        record.cnic = form.cnic.data
        record.department_id = int(form.department.data)
        record.qualification = form.qualification.data
        db.session.add(record)
        db.session.commit()
        return redirect(url_for('index'))

    form.first_name.data = record.first_name
    form.last_name.data = record.last_name
    form.dob.data = record.dob
    form.cnic.data = record.cnic
    form.department.data = str(record.department_id)
    form.qualification.data = record.qualification
    return render_template('updateEmployeeRecord.html', id = id, form = form)

#-------------------------------------------------------------------------------------------
@app.route('/delete', methods = ['GET', 'POST'])
def delete():
    form = SearchEmployee()
    if form.validate_on_submit():
        record = Employee.query.get(form.employeeId.data)
        if record:
            return redirect(url_for('deleteEmployeeRecord', id = form.employeeId.data))
        else:
            return '<p>Record doesnot exist! </p>'
    return render_template('delete.html', form = form)

#-------------------------------------------------------------------------------------------
@app.route('/deleteEmployeeRecord/<id>', methods = ['GET', 'POST'])
def deleteEmployeeRecord(id):
    form = DeleteEmployee()
    record = Employee.query.get(id)
    if record:
        if form.validate_on_submit():
            db.session.delete(record)
            db.session.commit()
            return redirect(url_for('index'))
    else:
        return '<p>Record doesnot exist! </p>'
    return render_template('deleteEmployeeRecord.html', form = form)

#-------------------------------------------------------------------------------------------


if __name__ == '__main__':
    app.run(debug = True)
