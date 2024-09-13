class LinkedListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_middle_node(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

"""
    TC: O(n)
    SC: O(1)
"""
