'''
예외가 발생하지 않았을 때만 실행하는 코드를 작성 하고 싶다
'''

try:
    print("Hello")
    # print(param)
except:
    print("Exception~~~")
else:
    print("Not Exception")