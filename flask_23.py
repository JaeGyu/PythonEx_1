from flask import Flask, current_app

app = Flask(__name__)

sess = "test"

with app.app_context():
    print(current_app.name)
    print(current_app)


@app.route("/")
def index():
    return sess

if __name__ == "__main__":
    sess = "hello"
    app.run(host = "0.0.0.0")