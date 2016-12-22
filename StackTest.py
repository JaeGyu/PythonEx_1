class Stack:

    store = []

    def push(self, data):
        self.store.append(data)

    def isEmpty(self):
        return len(self.store) == 0
    
    def pop(self):
        return self.store.pop()
    
    def top(self):
        return self.store[len(self.store) - 1]

    def size(self):
        return len(self.store)

def main():
    stack = Stack()
    print(stack.isEmpty())
    stack.push("a")
    print(stack.size())
    print(stack.isEmpty())
    print(stack.pop())
    print(stack.size())
    print(stack.isEmpty())

    stack.push("b")
    stack.push("c")
    print(stack.top())

if __name__ == "__main__":
    main()
