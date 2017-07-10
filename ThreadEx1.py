import threading


#아래는 쓰레드에서 실행 시킬 함수 이다.
def worker(count):
    print("name: %s, args: %s " % (threading.currentThread().getName(), count))

def main():
    for i in range(50):
        t = threading.Thread(target=worker, name="thread %i" % i, args=(i,)) 
        t.start()


if __name__ == "__main__":
    main()

