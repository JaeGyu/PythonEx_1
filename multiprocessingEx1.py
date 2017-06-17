import multiprocessing as mp 
import os 

def do_this(what):
    whoami(what)

def whoami(what):
    print("Process {} says: {}".format(os.getpid(), what))


if __name__ == "__main__":
    whoami("I'm the main program")
    for n in range(4):
        p = mp.Process(target = do_this, args=("I'm function {}".format(n),))
        p.start()