from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route("/")
@app.route("/<name>")
def index(name=None):
    return render_template('index.html', person=name)


@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        return redirect(url_for('index', name=user))
    else:
        user = request.args.get('username')
        return redirect(url_for('index', name=user))


if __name__ == '__main__':
    app.run(debug=True)