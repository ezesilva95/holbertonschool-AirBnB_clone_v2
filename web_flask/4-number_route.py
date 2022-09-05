#!/usr/bin/python3
"""
script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ” followed by the value of the text variable
(replace underscore _ symbols with a space )
/python/(<text>): display “Python ”, followed by the value of the text variabl
(replace underscore _ symb with space ) The default value of txt is “is cool”
/number/<n>: display “n is a number” only if n is an integer
"""

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


def hello_hbnb():
    """
    """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """
    """
    return "HBNB"


@app.route('/c/<text>')
def c_text(text):
    """
    """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python_text(text="is cool"):
    """
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def text_if_int(n):
    """
    """
    return "{:d} is a number".forat(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
