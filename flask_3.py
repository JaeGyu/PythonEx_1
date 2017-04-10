from flask import Flask, request, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello"

#URL의 변수부분을 추가 할 수 있다. 
@app.route("/user/<username>")
def show_user_profile(username):
    return "user name is %s." % username

'''
URL의 변수 부분에 타입(변환기라한다)를 지정해 줄수 있다. 
변환기는 3가지가 있다. 

string  : accepts any text without a slash (the default)
int     : accepts integers
float   : like int but for floating point values
path    : like the default but also accepts slashes
any     : matches one of the items provided
uuid    : accepts UUID strings

'''
@app.route("/post/<int:post_id>")
def show_post(post_id):
    return "id is %d" % (post_id + 1)

"""
아래 두개의 URL을 보면 패턴이 다르다
하나는 URL정의 뒤에 /가 있고 하나는 없다. 

http://localhost:5000/project 를 하면 Flask가 알아서 뒤에 /를 붙여준다.
그러나
http://localhost:5000/about/를 하면 404에러가 난다. 
"""
@app.route("/project/")
def project():
    return "The Project Page"

@app.route("/about")
def about():
    return "The about page"

@app.route("/login", methods = ['GET','POST'])
def login():
    if request.method == "POST":
        return "POST 입니다."
    else:
        return "POST가 아닙니다."

@app.route("/<id>")
def id(id):
    return id

'''
url_for(함수명, 인자)
'''
@app.route("/print_urls")
def print_urls():
    return "<br/>".join([url_for('about',next='/'),
    url_for("project"),
    url_for("id",id='alice')
    ])

@app.route("/reverse")
def reverse():
    message = request.values["message"]
    return "".join(reversed(message))

if __name__ == "__main__":
    app.run()



