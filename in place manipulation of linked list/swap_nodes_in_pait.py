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

def swap_pairs(head):
    dummy = LinkedListNode(0)
    dummy.next = head
    ptr = dummy

    while ptr.next and ptr.next.next:
        prev, cur = reverse_k(ptr.next, 2)

        last_reversed_node = ptr.next
        last_reversed_node.next = cur
        ptr.next = prev 
        ptr = last_reversed_node

    return dummy.next


"""
    TC: O(n)
    SC: O(1)
"""
