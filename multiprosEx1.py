import multiprocessing
import time 

class Process(multiprocessing.Process):
    def __init__(self,id):
        super(Process, self).__init__()
        self.id = id
    
    def run(self):
        time.sleep(int(self.id))
        print("I'm the process with id: {}".format(self.id))

if __name__ == "__main__":
    for i in range(20):
        p = Process(1)
        p.start()
        p.join()
    print("End!")
