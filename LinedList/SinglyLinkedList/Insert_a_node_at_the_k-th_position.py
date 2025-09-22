class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglylinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):   # insert at tail
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at_position(self, data, k):
        new_node = Node(data)
        if k == 1:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        pos = 1
        while current and pos < k - 1:
            current = current.next
            pos += 1

        if current is None:
            print(f"Position {k} is out of range")
            return

        new_node.next = current.next
        current.next = new_node


# Test
s = SinglylinkedList()
for v in [10, 20, 30, 40]:
    s.append(v)

print("Original list:")
s.traverse()

print("Insert 5 at position 1 (head):")
s.insert_at_position(5, 1)
s.traverse()

print("Insert 25 at position 3:")
s.insert_at_position(25, 3)
s.traverse()

print("Insert 50 at position 7 (tail):")
s.insert_at_position(50, 7)
s.traverse()

print("Try to insert at position 10 (invalid):")
s.insert_at_position(99, 10)
s.traverse()
