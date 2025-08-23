from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask7!"

@app.route("/about")
def about():
    return "about, Flask7!"

if __name__ == "__main__":
    app.run(debug=True)