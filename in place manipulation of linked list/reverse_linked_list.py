class LinkedListNode:
    # __init__ will be used to make a LinkedListNode type object.
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
            
def reverse(head):
    if not head:
        return head
    
    prev, cur = None, head
    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
    
    return prev

"""
    TC: O(n)
    SC: O(1)
"""