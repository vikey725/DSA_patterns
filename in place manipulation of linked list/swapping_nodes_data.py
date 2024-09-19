class LinkedListNode:
    # __init__ will be used to make a LinkedListNode type object.
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def swap_nodes(head, k):
    dummy = LinkedListNode(0)
    dummy.next = head
    ptr = dummy

    left, right = None, None

    while k:
        k -= 1
        ptr = ptr.next

    left = ptr
    right = dummy

    while ptr:
        ptr = ptr.next
        right = right.next
    
    # swap data
    temp = left.data
    left.data = right.data
    right.data = temp

    return head 

"""
    TC: O(n)
    SC: O(n)
"""