from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def helloworld():
    return "Hello"

@app.route("/member", methods=["GET"])
def getMember():
    result = []
    mem = {"name":"alice", "age":27}
    result.append(mem)
    return json.dumps(result)

def main():
    app.run(debug=True, host="0.0.0.0", port=5009)

if __name__ == "__main__":
    main()