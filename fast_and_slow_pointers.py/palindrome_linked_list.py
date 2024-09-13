class LinkedListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def palindrome(head):
    # find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # print(slow.data)
    # reverse 2nd half
    prev, current = None, slow
    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
        
    # print(prev.data)

    # check palindrome
    left, right = head, prev
    while right:
        if left.data != right.data:
            return False
        left = left.next
        right = right.next
    
    return True

"""
    TC: O(n)
    SC: O(1)
"""