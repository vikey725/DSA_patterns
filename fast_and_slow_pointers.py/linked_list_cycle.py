def detect_cycle(head):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True 
    
    return False
    

"""
    TC: O(n)
    SC: O(1)
"""
