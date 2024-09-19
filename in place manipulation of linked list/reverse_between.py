class LinkedListNode:
    # __init__ will be used to make a LinkedListNode type object.
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def reverse_k(ptr, k):
    prev, cur = None, ptr
    while k:
        k -= 1
        temp = cur.next
        cur.next = prev 
        prev = cur 
        cur = temp

    return prev, cur

def reverse_between(head, left, right):
    dummy = LinkedListNode(0)
    dummy.next = head
    ptr = dummy

    for i in range(left - 1):
        ptr = ptr.next
    
    
    prev, cur = reverse_k(ptr.next, right - left + 1)

    last_node_of_reversed = ptr.next
    last_node_of_reversed.next = cur
    ptr.next = prev

    return dummy.next


"""
    TC: O(n)
    SC: O(1)
"""
