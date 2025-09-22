# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution class
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        current = head
        while current:
            vals.append(current.val)
            current = current.next
        return vals == vals[::-1]

# Helper function to create linked list from Python list
def create_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Example usage
lst1 = [1, 2, 3, 2, 1]
lst2 = [1, 2, 3]

head1 = create_linked_list(lst1)
head2 = create_linked_list(lst2)

s = Solution()
print(s.isPalindrome(head1))  # True
print(s.isPalindrome(head2))  # False
