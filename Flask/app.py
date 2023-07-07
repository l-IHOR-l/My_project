from flask import Flask, render_template
from operator import *

app = Flask(__name__)


@app.route('/')
def calculate():
    numbers = [1, 10, 100]
    return render_template('index.html',
                           numbers=numbers)


# @app.route('/<a>/')
# def calc(a):
#     return f"{eval(a.replace(':', '/'))}"


if __name__ == '__main__':
    app.run(debug=True)
