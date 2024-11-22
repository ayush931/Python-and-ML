# App routing means mapping the url to a specific function that will handle the logic for that url

from flask import Flask

app = Flask(__name__)

# Define a route with a dynamic parameter 'id of type integer

@app.route('/post/<int:id>')
def show_post(id):
    # Return a string with the id
    return f'This post has the id {id}'

# Define a route with a dynamic parameter 'username' of type string
@app.route('/user/<string:username>')
def show_user(username):
    # Return a string with the username
    return f'This user has the username {username}'

# Define a route for '/hello' endpoint
@app.route('/hello')
def hello():
    return 'Hello World'

# Define the default route for the root URL '/'
@app.route('/')
def index():
    return 'Homepage of the application'

# Run the app
if __name__ == '__main__':
    app.run(debug=True)