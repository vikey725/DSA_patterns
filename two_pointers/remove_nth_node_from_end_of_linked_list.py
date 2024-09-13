class LinkedListNode:
    # __init__ will be used to make a LinkedListNode type object.
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def remove_nth_last_node(head, n):
    if not head:
        return head
    
    dummy = LinkedListNode(0)
    dummy.next = head

    slow, fast = dummy, dummy
    for _ in range(n):
        fast = fast.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next

    return dummy.next

"""
    TC: O(n)
    SC: O(1)
"""
