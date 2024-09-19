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

def reverse_k_groups(head, k):
    dummy = LinkedListNode(0)
    dummy.next = head 
    ptr = dummy

    while True:
        tracker = ptr 
        for i in range(k):
            if not tracker:
                break
            tracker = tracker.next 

        if not tracker:
            break

        prev, cur = reverse_k(ptr.next, k)

        last_node_of_reversed = ptr.next
        last_node_of_reversed.next = cur 
        ptr.next = prev 
        ptr = last_node_of_reversed
    
    return dummy.next

"""
    TC: O(n)
    SC: O(1)
"""

        

