
class Queue():
    def __init__(self):
        self.store = []

    def enQueue(self, num):
        self.store.append(num)

    def deQueue(self):
        result = self.store[0]
        del self.store[0]
        return result

    def toString(self):
        return self.store


if __name__ == "__main__":
    q = Queue()

    q.enQueue(22)
    q.enQueue(67)
    print(q.toString())
    q.deQueue()

    print(q.toString())