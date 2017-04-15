from flask import Flask

app = Flask(__name__)

'''
HTTP 요청 전에 실행되는 함수는 before_first_request와 before_request 데코레이터를 사용해 추가할 수 있으며
이 함수는 어떠한 인자도 전달 할 수 없다. 

before_first_request와 before_request 데코레이터를 사용한 함수는 Flask 인스턴스 객체 내에서
before_first_request_funcs, before_request_funcs 리스트 타입 변수에 요소로 추가되어 저장 된다.
'''

@app.route("/")
def http_prepost():
    return "/"

'''
웹 애플리케이션 기동 이후 가장 처음에 들어오는 HTTP요청에만 실행 됩니다.
'''
@app.before_first_request
def before_first_request():
    print("앱이 기동되고 나서 첫 번째 HTTP 요청에만 응답합니다.")

'''
동일한 데코레이션을 여러개 사용해도 된다. 
'''
@app.before_first_request
def before_first_request2():
    print("앱이 기동되고 나서 첫 번째 HTTP 요청에만 응답합니다.2222222")

'''
매 HTTP요청이 들어올 때마다 실행 됩니다.
'''
@app.before_request
def before_request():
    print("매 HTTP 요청이 처리되기 전에 실행됩니다.")

'''
매 HTTP 요청이 끝나 브라우저에 응답하기 전에 실행 됩니다. 
브라우저에 날라가기 직전에 호출이 되기 떄문에 
response를 인자로 받는다.
여기서 response에 속한 데이터를 가공하건 할 수 있다.
그래서 개발자가 반드시 response를 다시 반환 해 줘야 한다. 
안그러면 500에러 발생 한다.
'''
@app.after_request
def after_request(response):
    print("매 HTTP 요청이 처리되고 나서 실행됩니다.")
    print(response)
    return response

'''
HTTP 요청의 결과가 블라우저에 응답한 다음 실행 됩니다. 
'''
@app.teardown_request
def teardown_request(exception):
    print("매 HTTP 요청의 결과가 브라우저에 응답하고 나서 호출됩니다.")

'''
HTTP요청이 완전히 완료되면 실행되며, 애플리케이션 컨텍스트 내에서 실행 됩니다.
teardown_request 다음에 호출되는 데코레이터이다. 개별 HTTP 요청의 처리가 완전히 끝나고
Flask 애츨리케이션 컨텍스트가 끝날 때마다 실행 되는데, 애플리케이션 코드에서는 
with  app.app_context() 블록 안에서 사용된 객체를 제가해야 할 때 등 
제한적인 용도로 사용하게 된다.
'''
@app.teardown_appcontext
def teardown_appcontext(exception):
    print("HTTP 요청의 애플리케이션 컨텍스트가 종료될 떄 실행 됩니다.")

@app.route("/sample")
def sample():
    return "샘플 요청 입니다."

if __name__ == "__main__":
    app.run(host = "0.0.0.0")