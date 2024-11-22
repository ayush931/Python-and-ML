from flask import Flask

# Instantiate the Flask app

app = Flask(__name__)

@app.route("/") #Home directory
def hello():
    return 'Hello learner. I am enjoying flask'

# If you want to run this app, you must call the run()
if __name__ == "__main__":
    app.run(debug=True, port=4015)