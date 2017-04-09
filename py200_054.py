class Add:
    def add(self, n1, n2, n3 = 0):
        return n1 + n2 + n3


class Calculator(Add):
    def sub(self, n1, n2):
        return n1 - n2


o = Calculator()

print(o.add(1, 2))
print(o.sub(1, 2))
print(o.add(1, 2, 3))
