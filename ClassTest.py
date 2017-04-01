class Dog:
    def __init__(self):
        self.name = "happy"
    
    def __call__(self):
        print(self.name)

def main():
    Dog()

if __name__ == "__main__":
    main()