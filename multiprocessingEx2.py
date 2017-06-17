import multiprocessing as mp 
import os, time

def whoami(name):
    print("I'm {}, in process {}".format(name, os.getpid()))

def loopy(name):
    whoami(name)
    start = 1
    stop = 1000000
    for i in range(start, stop):
        print("\tNumber {} of {}. Honk!".format(i, stop))
        time.sleep(1)

if __name__ == "__main__":
    whoami("main")
    p = mp.Process(target = loopy, args=("loopy",)) #args에서 ,는 무조건 해줘야 한다. 
    p.start() 
    time.sleep(5)
    p.terminate()