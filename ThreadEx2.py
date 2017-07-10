import threading

"""
아래는 threading.Thread 클래스를 상속 받는 클래스에 원하는 내용을 정의 하여
사용한다. 
run()은 오버라이딩 해준다.
"""
class Worker(threading.Thread):

    def __init__(self, args, name=""):
        #현재 클래스에  init를 만들면 상위 클래스의 init를 호출해야 한다.
        threading.Thread.__init__(self)
        self.args = args
    
    #threading.Thread 클래스의 run 메서드를 오버라이딩 한다. 
    def run(self):
        print("name : %s, argument : %s" % (threading.currentThread().getName(), self.args[0]))
    

def main():
    for i in range(50):
        t = Worker(name="thread %i" % i, args=(i,))
        t.start()

if __name__ == "__main__":
    main()

