from flask import Flask

app = Flask(__name__)

@app.route("/board", methods=['GET'])
def board_list_get():
    pass

@app.route("/board", methods=['POST'])
def board_list_post():
    pass

#아래와 같은 방식으로 methods안에 여러개를 사용하는 것은 권장 하지 않는다.
@app.route("/member", methods=['POST','GET'])
def member_list_get_post():
    pass

if __name__ == "__main__":
    app.run()