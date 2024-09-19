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

def reverse_even_length_groups(head):
    dummy = LinkedListNode(0)
    dummy.next = head

    ptr = dummy 
    k = 1

    while True:
        tracker = ptr
        count = 0
        for i in range(k):
            tracker = tracker.next
            if not tracker:
                break
            count += 1
        
        reverse = False
        if count != 0 and count % 2 == 0:
            reverse = True

        if not reverse:
            ptr = tracker
        else:
            prev, cur = reverse_k(ptr.next, count)

            last_node_of_reversed = ptr.next
            last_node_of_reversed.next = cur
            ptr.next = prev
            ptr = last_node_of_reversed
        
        reverse = not reverse
        k += 1
        if not tracker:
            break

    return dummy.next

"""
    TC: O(n)
    SC: O(1)
"""

