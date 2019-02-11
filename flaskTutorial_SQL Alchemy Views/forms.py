from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, RadioField, SubmitField, BooleanField
from wtforms.validators import DataRequired


################################################
############## Employee forms ##################
################################################
class AddEmployee(FlaskForm):
    first_name = StringField('First Name', validators = [DataRequired()])
    last_name = StringField('Last Name', validators = [DataRequired()])
    dob = StringField('DOB (dd-mm-yy)', validators = [DataRequired()])
    cnic = StringField('cnic', validators = [DataRequired()])
    qualification = RadioField('Recent Qualification : ', choices = [('bs', 'Bachelors'), ('ms','Masters'), ('phd', 'PHD')], validators = [DataRequired()])
    department = SelectField('Department', choices = [('1', 'Computer Sciences'), ('2', 'Electrical Engineering'),
                            ('3', 'Environmental Sciences'), ('4', 'Mechanical Engineering'), ('5', 'Software Engineering')], validators = [DataRequired()])
    submit = SubmitField('Save Record')
    updateSubmit = SubmitField('Update')

#--------------------------------------------------------------------
class SearchEmployee(FlaskForm):
    employeeId = IntegerField('Employee ID', validators = [DataRequired()])
    submit = SubmitField('Search')

#--------------------------------------------------------------------
class DeleteEmployee(FlaskForm):
    confirm = BooleanField('Are You Sure you want to delete the record? This action cannot be undone!', validators = [DataRequired()])
    submit = SubmitField('Delete')

#--------------------------------------------------------------------
