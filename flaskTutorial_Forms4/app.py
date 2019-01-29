from flask import Flask, render_template, session, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, RadioField, TextAreaField, BooleanField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mySecretKey'

class SignUpForm(FlaskForm):
    firstName = StringField('First Name', validators = [DataRequired()])
    lastName = StringField('Last Name', validators = [DataRequired()])
    location = SelectField('Country', choices = [('none', ' --Please Select your country-- '), ('in', 'India'), ('pk', 'Pakistan'),('uk', 'United Kingdom'),('us', 'United States'), ('other', 'Other')])
    gender = RadioField('Gender', choices = [('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    address = TextAreaField('Address')
    agreeToTerms = BooleanField('Agree to Terms and Conditions?', validators = [DataRequired()])
    submit = SubmitField('SignUp')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/SignUp', methods = ['GET', 'POST'])
def SignUp():
    form = SignUpForm()
    if form.validate_on_submit():
        session['fName'] = form.firstName.data
        session['lName'] = form.lastName.data
        session['gender'] = form.gender.data
        session['location'] = form.location.data
        session['address'] = form.address.data
        session['termAgreement'] = form.agreeToTerms.data
        return redirect(url_for('thankyou'))
    return render_template('SignUp.html', form = form)

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')


if __name__ == '__main__':
    app.run(debug = True)
