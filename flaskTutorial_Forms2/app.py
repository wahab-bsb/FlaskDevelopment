from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mySecretKey'

class SignUpForm(FlaskForm):
    firstName = StringField('First Name : ')
    lastName = StringField('Last Name : ')
    submit = SubmitField('SignUp')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signUp', methods = ['GET', 'POST'])
def signUp():
    firstName = False
    lastName = False
    form = SignUpForm()
    if form.validate_on_submit:
        firstName = form.firstName.data
        lastName = form.lastName.data
        form.firstName.data = ""
        form.lastName.data = ""
    return render_template('signUp.html', form = form, firstName = firstName, lastName = lastName)


if __name__ == '__main__':
    app.run(debug = True)
