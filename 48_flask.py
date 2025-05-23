from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route("/home")
def hello_home():
    return render_template("index.html")

@app.route("/<name>")
def user(name):
    return f'Hello {name}'

@app.route('/home/test')
def test_home():
    return redirect(url_for("hello_home"))

if __name__ == "__main__":
    app.run(debug=True)