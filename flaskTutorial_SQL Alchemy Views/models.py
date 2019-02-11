from app import db

# Models
#-------------------------------------------------------------------------------------------------------------
class Departments(db.Model):
    __tablename__ = 'Departments'

    department_id = db.Column(db.Integer, primary_key = True)
    department_name = db.Column(db.Text)

    def __init__(self, name):
        self.department_name = name

    def __repr__(self):
        return f'Department ID : {self.department_id}, Department Name : {self.department_name}'
#-------------------------------------------------------------------------------------------------------------
class Employee(db.Model):
    __tablename__ = 'Employee'

    employee_id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    dob = db.Column(db.Text)
    cnic = db.Column(db.Text)
    qualification = db.Column(db.Text)
    department = db.relationship('Departments', backref = 'Employee', uselist = False)
    department_id = db.Column(db.Integer, db.ForeignKey('Departments'))

    def __init__(self, first_name, last_name, dob, cnic, qualification, department_id):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.cnic = cnic
        self.qualification = qualification
        self.department_id = department_id

    def __repr__(self):
        if self.department:
            return f'ID: {self.employee_id}, Name : {self.first_name} {self.last_name}, DOB : {self.dob}, Cnic : {self.cnic}, Qualification : {self.qualification}, Department ID: {self.department_id}, Department Name : {self.department.department_name}'
        return f'ID: {self.employee_id}, Name : {self.first_name} {self.last_name}, DOB : {self.dob}, Cnic : {self.cnic}, Qualification : {self.qualification}, Department Not Assigned'
#------------------------------------------------------------------------------------------------------------
