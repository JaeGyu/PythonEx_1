def deco(func):
    def new_func(*args, **kargs):
        print("hello")
        func(*args, **kargs)
        print("end")
    return new_func
    

@deco
@deco
@deco
def print_hi(name, age, addr):
    print("이름 : ", name, " 나이 : ",age," 주소 : ",addr)

@deco
def print_hi2():
    print("just~~")

def main():
    print_hi("alice",11,"la")
    print("-" * 60)
    print_hi2()

if __name__ == "__main__":
    main()