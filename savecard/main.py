from flask import Flask, render_template, request, url_for, redirect
import datetime

app = Flask(__name__)

@app.route("/")
def index(name=None):
    idade = datetime.datetime.now().year - 2003
    return render_template('index.html', idade=idade)


@app.route("/card")
def card():
    return render_template('card.html')


if __name__ == '__main__':
    app.run(debug=True)