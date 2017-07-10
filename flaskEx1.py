from flask import Flask
from flask import request

#request객체는 요청 데이터를 파싱해서 전역 객체로 데이터에 접근하게 해준다.

#플라스크 앱을 생성합니다.
app = Flask(__name__)

#편의를 위한 디버그 모드를 활성화 합니다.
#코드를 수정 할 때마다 바로바로 웹 애플리케이션에 반영한다.
#파이썬 프로그램을 종료했다가 다시 실행할 필요 없이 파일만 수정하면 된다.
app.debug = True

#URL 경로에 따라 실행할 함수에 데코레이터를 사용합니다. 테코레이터의 파라미터는 URL 경로 입니다.
@app.route("/")

#앞 경로에 접근하면 실행할 함수입니다.
def hello():
    return "Hello World"

@app.route("/hello/<name>")
def hello_to(name):
    return "<h1>Hello, {}<span style='color:red'>!</span></h1>".format(name)

@app.route("/hello")
def hello_to_get_param():
    #/hello?name=miku와 같은 형식의 요청을 받아서
    #?name=<이름>의 값이 오면, <이름>을 name에 저장합니다.
    name = request.args.get("name")
    return "<h1 style='color:blue'>Hello, {}!</h1>".format(name)

#이 파일을 바로 실행할 때 함께 실행할 코드를 적습니다.
if __name__ == "__main__":
    #앞에서 생성한 플라스크 애플리케이션을 실행 합니다.
    app.run()

