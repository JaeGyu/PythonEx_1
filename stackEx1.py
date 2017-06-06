
class Stack():
    def __init__(self):
        self.store = []

    def push(self, num):
        self.store.append(num)

    def pop(self):
        return self.store.pop()

    def size(self):
        return len(self.store)
    
    def toString(self):
        return self.store

    def top(self):
        return self.store[-1]

if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    print(s.top())
    s.push(5)
    print(s.size())
    print(s.toString())
    s.pop()
    print(s.toString())
    print(s.size())
