from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/signUp')
def signUp():
    return render_template('signUp.html')

@app.route('/thankyou')
def thankyou():
    firstName = request.args.get('first')
    lastName = request.args.get('last')
    return render_template('thankyou.html', firstName = firstName, lastName = lastName)

if __name__ == '__main__':
    app.run(debug = True)
