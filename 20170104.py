
a = 1
b = a
print(b)

b = 2
print("b : ", b)
print("a : ", a)

class A:

    a = ""

    def setA(self, a):
        self.a = a

    def getA(self):
        return self.a
        

aa = A()
aa.setA("aaa")
print(aa.getA())

bb = aa
bb.setA("bbb")
print("bb.getA() :: ",bb.getA())
print("aa.getA() ::",aa.getA())




