import flask
from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return"Successfully Created Flask Application"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)