# singly circular linked list

class CNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = CNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            return
        self.tail.next = new_node
        new_node.next = self.head
        self.tail = new_node

    def traverse(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(head)")

cll = CircularLinkedList()
for v in [10, 20, 30, 40, 50]:
    cll.append(v)

cll.traverse()

# Doubly Circular Linked List

class DCNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = DCNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        new_node.next = self.head
        self.head.prev = new_node
        self.tail = new_node

    def traverse_forward(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(head)")

    def traverse_backward(self):
        if self.tail is None:
            print("List is empty")
            return
        current = self.tail
        while True:
            print(current.data, end=" -> ")
            current = current.prev
            if current == self.tail:
                break
        print("(tail)")

dcll = DoublyCircularLinkedList()
for v in [10, 20, 30, 40, 50]:
    dcll.append(v)

print("Forward:")
dcll.traverse_forward()

print("Backward:")
dcll.traverse_backward()
