class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglylinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
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



s = SinglylinkedList()
for v in [10, 20, 30, 40, 50]:
    s.append(v)

print("Original list:")
s.traverse()

print("After inserting 5 at head:")
s.insert_at_head(5)
s.traverse()
