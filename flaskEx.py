from flask import Flask

app = Flask(__name__)


html = """
<html>
<body>
    <ul>
        <li>asdfa</li>
        <li>asdfas</li>
        <li>asdfas</li>
        <li>asdfas</li>
    </ul>

</body>
</html>

"""

@app.route("/<name>")
def hello(name):
    return "hello " + name

if __name__ == "__main__":
    app.run(debug=True)

