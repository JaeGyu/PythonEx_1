import multiprocessing as mp 

lock = mp.Lock()

class Process(mp.Process):

    def __init__(self, counter):
        super(Process, self).__init__()
        self.counter = counter

    def run(self):
        for i in range(1000):
            with lock: #잠금 획득
                self.counter.value += 1
            #잠금 해제 
    

def main():
    counter = mp.Value('i', lock=True)
    counter.value = 0

    processes = [Process(counter) for i in range(4)]
    [p.start() for p in processes]
    [p.join() for p in processes]
    print(counter.value)

if __name__ == "__main__":
    main()