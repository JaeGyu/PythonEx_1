class Add:
    def add(self, n1, n2, n3=0):
        print("add of Add")
        return n1 + n2 + n3


class Add2:
    def add(self, n1, n2, n3=0):
        print("add of Add2")
        return n1 * n2

# 부모들 중 같은 시그너쳐의 메서드가 있다면 먼저 상속선언된 부모의 메서드가 우선시 되는 것 같다
class Calculator(Add2, Add):
    def sub(self, n1, n2):
        return n1 - n2


o = Calculator()

print(o.add(1, 2))
print(o.sub(1, 2))
# print(o.add(1, 2, 3))
