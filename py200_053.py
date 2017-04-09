class MyClass:
    
    def __init__(self):
        print("생성자가 호출 되었네요!")
    
    def __del__(self):
        print("소멸자가 호출 되었네요!")
    

o = MyClass()
del o