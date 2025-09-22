# Program: ReverseSinglyLinkedList

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Append a node at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Print the linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next   # save the next node
            current.next = prev        # reverse the link
            prev = current             # move prev one step
            current = next_node        # move current one step
        self.head = prev               # update head to the new front


# -------- Driver Code --------
if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.append(10)
    sll.append(20)
    sll.append(30)
    sll.append(40)

    print("Original Linked List:")
    sll.display()

    sll.reverse()

    print("Reversed Linked List:")
    sll.display()
