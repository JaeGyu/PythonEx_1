#_*_ coding: UTF-8 _*_

"""
((()))  -> YES
()) -> NO
"""

def check(value):
    """This function is problem solving using stack structure."""
    cnt = 0
    for i in value:
        if i == "(":
            cnt = cnt+1
        else:
            if value[cnt-1] == "(":
                cnt -= 1
            else:
                return "NO"
    if cnt == 0:
        return "YES"
    else:
        return "NO"

def check2(value):
    cnt = 0

    for e in value:
        if e == "(":
            cnt += 1
        elif value[cnt-1] == "(":
            cnt -= 1
        else:
            return "NO"
        
    if cnt == 0:
        return "YES"
    else:
        return "NO"


def main():
    """main function"""
    print("()", check("()"))
    print(")", check(")"))
    print("(())", check("(())"))
    print("(()))", check("(()))"))
    print("()()", check("()()"))
    print("(())(())()(", check("(())(())()("))

def main2():
    print(check2("()()"))
    print(check2(")"))
    print(check2("((())))"))
    print(check2("((()))"))

if __name__ == "__main__":
    main2()
