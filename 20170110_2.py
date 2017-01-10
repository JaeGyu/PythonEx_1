def deco(func):
    def new_func(*args, **kargs):
        print("hello")
        func(*args, **kargs)
        print("end")
    return new_func
    

@deco
def print_hi(name, age, addr):
    print("이름 : ", name, " 나이 : ",age," 주소 : ",addr)

def main():
    print_hi("alice",11,"la")

if __name__ == "__main__":
    main()