#_*_ coding: UTF-8 _*_

def sum(a,b):
    return a+b

def sumToMany(*args):
    sum = 0
    for i in args:
        sum+=i
    return sum

def main():
    print(sum(4,5))
    print(sumToMany(1,2,3,4,5,6,7,8,9,10))

if __name__ == "__main__":
    main()