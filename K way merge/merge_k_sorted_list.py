import heapq

class LinkedListNode:
    # __init__ will be used to make a LinkedListNode type object.
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def merge_k_lists(lists):
    min_heap = [(node.head.data, idx, node.head) for idx, node in enumerate(lists) if node and node.head is not None]
    heapq.heapify(min_heap)

    dummy = LinkedListNode(0)
    cur = dummy
    while min_heap:
        _, i, node = heapq.heappop(min_heap)
        cur.next = node
        cur = cur.next

        if node.next:
            heapq.heappush(min_heap, (node.next.data, i, node.next))

    return dummy.next

"""
    TC: O(n log m)
    SC: O(m)
"""

