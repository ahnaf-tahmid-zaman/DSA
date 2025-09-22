class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = DNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def traverse_forward(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def traverse_backward(self):
        current = self.tail
        while current:
            print(current.data, end=" -> ")
            current = current.prev
        print("None")

dll = DoublyLinkedList()
for v in [10, 20, 30, 40, 50]:
    dll.append(v)

print("Forward:")
dll.traverse_forward()

print("Backward:")
dll.traverse_backward()
