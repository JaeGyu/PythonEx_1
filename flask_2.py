from flask import Response, make_response, Flask

app = Flask(__name__)

@app.route("/")
def response_test():
    custom_response = Response("Custom Response", 200, {
        "Program":"Flask Web Application"
    })

    return make_response(custom_response)

@app.route("/str")
def str_response_test():
    return make_response("Custom Respon by Str")

@app.route("/wsgi")
def wsgi_response_test():
    def application(environ, start_response):
        response_body = "The request method was {}".format(environ["REQUEST_METHOD"])
        status = "200 OK"
        response_headers = [("Content-Type","text/plain"),
        ("Content-Length", str(len(response_body)))]

        start_response(status, response_headers)
        return [response_body]
    return make_response(application)

@app.route("/tuple")
def tuple_response_test():
    return make_response(("<h1>Tuple Custom Response</h1>", "OK", {
        "response_method":"Tuple Response"
    }))

if __name__ == "__main__":
    app.run()

