
'''
py200_mypackage라는 패키지(폴더) 아래의 p200_mylib라는 모듈 안의 add 함수를 import 한다

파이썬에서 폴더를 패키지로 인식시키기 위해서는 폴더안에 __init__.py 파일을 만들어야 한다.
__init__.py의 내용은 아무거나 상관 없다 
    
'''
from py200_mypackage.p200_mylib import add

print(add(1,2))