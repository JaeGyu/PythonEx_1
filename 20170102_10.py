class GlobalTest:
    def __init__(self):
        self.a = 0

    def setA(self):
        self.a += 100
    
    def setB(self):
        self.a += 50
    
    def get(self):
        return self.a

def main():
    g = GlobalTest()
    g.setA()
    g.setB()
    print(g.get())

if __name__ == "__main__":
    main()

