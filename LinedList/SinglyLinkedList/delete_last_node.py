# delete_last_node.py

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
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

    def delete_last(self):
        if self.head is None:
            print("List is empty. Nothing to delete.")
            return

        if self.head.next is None:
            # Only one node
            print(f"Deleting node with value: {self.head.data}")
            self.head = None
            return

        # Traverse to second last node
        current = self.head
        while current.next.next:
            current = current.next

        print(f"Deleting node with value: {current.next.data}")
        current.next = None  # Remove last node


# Test
if __name__ == "__main__":
    s = SinglyLinkedList()
    for v in [10, 20, 30, 40, 50]:
        s.append(v)

    print("Original list:")
    s.traverse()

    s.delete_last()
    print("After deleting last node:")
    s.traverse()

    s.delete_last()
    print("After deleting last node again:")
    s.traverse()
