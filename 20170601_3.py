class Person:
    def __init__(self,name):
        self.name = name
    
    def getName(self):
        return self.name
    
    def setName(self,name):
        self.name = name

    
def main():
    p = Person("han") 
    print(p.getName())
    p.setName("alice")
    print(p.getName())

if __name__ == "__main__":
    main()