def aop_log(func):
    def temp(num):
        print("-"*60)
        print("info - %s" % func)
        func(num)
        print("info - %s" % "END")
        print("-"*60)
    return temp

@aop_log
def process(num):
    for i in range(1,num+1):
        print("*" * i)
    
def process2(num):
    for i in range(1,num+1):
        print("*"*i)

def main():
    process(10)
    f = aop_log(process2)
    f(10)
    

if __name__ == "__main__":
    main()
    