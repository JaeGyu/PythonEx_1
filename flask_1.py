'''
플라스크는 전역적으로 데이터를 보관하고 사용할 수 있도록 
글로벌 객체를 제공한다. 

이 글로벌객체는 애플리케이션 전체에 걸쳐 전역을 제공하는 것인가?

파이썬은 언어 특성상 전역 영역은 애플리케이션 전체에 걸친 영역이 아닌 모듈 단위의 영역으로 한정한다. 
그런데 일걸쓰면 애플리케이션레벨에서 글로벌을 사용할 수 있는 것인가?

글로벌 객체는 애플리케이션 전반에서 공유해야 할 데이터를 저장해두고 사용하는 데 효율적이지만, 글로벌 객체에
저장한 속성에 다수의 동시접근이 이뤄지면 애플리케이션 운용에 문제가 발생할 수 있습니다. 

일반적으로 웹 애플리케이션이 동작하는 동안 유지되어야 하는 값을 저장한다. 
대표적 예로 db연결 객체를 저장한다.

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

#http 요청이 들어올때마다 아래의 데코레이터가 실행됨
@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
      #전역 객체 g에서 'db'속성을 가져오며 없다면 None를 반환해라!
    db = getattr(g, 'db', None)

    if db is not None:
        db.close()

'''

from flask import g 
    