from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    #return 'Hello, World!'
    return render_template('indextut.html')

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello {}!!<h1>'.format(name)

if __name__ == "__main__":
    app.run(debug=True, port=8000)