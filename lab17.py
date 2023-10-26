from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def hello():
    p1 = '<p>Hope R. : jm</p>'
    p2 = '<p>Jack M. : math</p>'
    return p1 + p2


@app.route('/hope')
def t_test():
    return render_template('f1.html')