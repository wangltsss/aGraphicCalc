from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/graph')
def hello_world():  # put application's code here
    return render_template("index.html", x=[1,2,3,4,5], y=[6,7,8,9,10])


if __name__ == '__main__':
    app.run()
