def deco(func):
    def temp():
        print("-"*60)
        func()
        print("-"*60)
    return temp

@deco
def print_h1():
    print("body")

def main():
    print_h1()

if __name__ == "__main__":
    main()