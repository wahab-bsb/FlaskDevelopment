from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    pageTitle = 'Home'
    return render_template('index.html', pageTitle = pageTitle)

@app.route('/page2')
def listDisplayView():
    pageTitle = 'List Display'
    myList = ['dummy Lorem ipsum words', 'Lorem ipsum dolor sit amet', 'Praesent eget condimentum nisi', 'Phasellus venenatis est vel pretium vestibulum', 'Morbi placerat ipsum sit amet sem semper luctus']
    return render_template('listDisplay.html', myList = myList, pageTitle = pageTitle)

if __name__ == '__main__':
    app.run(debug = True)
