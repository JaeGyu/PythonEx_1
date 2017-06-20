import random as rnd 

def get():
    a = list(range(1,46))
    rnd.shuffle(a)
    return a[0:6]

if __name__ == "__main__":
    for i in range(10):
        print(get())
