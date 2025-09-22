# delete_node_by_value.py

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

    def delete_by_value(self, value):
        if self.head is None:
            print("List is empty. Nothing to delete.")
            return

        # Case 1: if head contains the value
        if self.head.data == value:
            print(f"Deleting node with value: {value}")
            self.head = self.head.next
            return

        # Traverse to find the node before the one to delete
        current = self.head
        while current.next and current.next.data != value:
            current = current.next

        # Value not found
        if current.next is None:
            print(f"Value {value} not found in the list.")
            return

        # Delete node
        print(f"Deleting node with value: {value}")
        current.next = current.next.next


# Test
if __name__ == "__main__":
    s = SinglyLinkedList()
    for v in [10, 20, 30, 20, 40]:
        s.append(v)

    print("Original list:")
    s.traverse()

    s.delete_by_value(20)
    print("After deleting first occurrence of 20:")
    s.traverse()

    s.delete_by_value(10)
    print("After deleting first occurrence of 10 (head):")
    s.traverse()

    s.delete_by_value(50)
    print("Try deleting value not in list:")
    s.traverse()
