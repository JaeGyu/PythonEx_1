import threading as thd

def do_this(what):
    whoami(what)

def whoami(what):
    print("Thread {} says: {}".format(thd.current_thread(), what))

if __name__ == "__main__":
    whoami("I'm the main program.")

    for n in range(4):
        t = thd.Thread(target=do_this, args=("I'm function {}".format(n),))
        t.start()

