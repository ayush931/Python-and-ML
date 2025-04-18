from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = "my_secret_key"

users = {
    "ayush": "12345",
    "user1": "password1"
}

@app.route("/")
def view_form():
    return render_template('login.html')

@app.route("/handle_get", methods=['GET'])
def handle_get():
    if request.method == "GET":
        username = request.args['username']
        password = request.args['password']
        print(username, password)
        if username in users and users[username] == password:
            return '<h1>Welcome!!!</h1>'
        else:
            return '<h1>invalid credentials!!!</h1>'
    else:
        return render_template('login.html')
        
        
@app.route("/handle-post", methods=['POST'])
def handle_post():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username, password)
        if username in users and users[username] == password:
            return '<h1>Welcome!!!</h1>'
        else:
            return '<h1>invalid credentials!!!</h1>'
    else:
        return render_template('login.html')
    
if __name__ == "__main__":
    app.run()