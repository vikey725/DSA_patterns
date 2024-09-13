def is_palindrome(string):
    def helper(l, r):
        while l < r:
            if string[l] != string[r]:
                return False
            l += 1
            r -= 1
        return True
    
    s, e = 0, len(string) - 1
    while s < e:
        if string[s] != string[e]:
            return helper(s + 1, e) or helper(s, e - 1)
        s += 1
        e -= 1
    
    return True

"""
    TC: O(n)
    SC: O(1)
"""

