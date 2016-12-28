from flask import Flask

app = Flask(__name__)

@app.route("/")
def helloworld():
    return "Hello"

def main():
    app.run(debug=True, host="0.0.0.0", port=5009)

if __name__ == "__main__":
    main()