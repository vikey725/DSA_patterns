class LinkedListNode:
    # __init__ will be used to make a LinkedListNode type object.
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def reorder_list(head):
    # find middle
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # reverse second half
    prev, cur = None, slow
    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur 
        cur = temp 

    # merge 
    first, second = head, prev

    while second.next:
        temp1 = first.next
        temp2 = second.next
        first.next = second 
        second.next = temp1
        first = temp1 
        second = temp2 

    return head 

"""
    TC: O(n)
    SC: O(1)
"""