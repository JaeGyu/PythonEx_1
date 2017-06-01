class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

def init_list():
    global node1,node2,node3
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    
    node1.next = node2
    node2.next = node3
    
    
def main():
    init_list()
    node = node1
    while node:
        print(node.data)
        node = node.next

if __name__ == "__main__":
    main()