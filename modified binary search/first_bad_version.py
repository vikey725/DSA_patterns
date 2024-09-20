import random


class ApiCall:
    def is_bad(v):
        return False
    
api_call = ApiCall()


def is_bad_version(v, n): # is_bad_version() is the API function that returns true or false depending upon whether the provided version ID is bad or not
    return api_call.is_bad(v)

def first_bad_version(n):
    api_call_count = 0
    left, right = 1, n
    while left <= right:
        mid = (left + right) // 2

        if is_bad_version(mid):
            right = mid - 1
        else:
            left = mid + 1

        api_call_count += 1
    return [left, api_call_count]

"""
    TC: O(log n)
    SC: O(1)
"""
