def get_subsets(arr):
    subsets = []
    def helper(sub, idx):
        if idx == len(arr):
            subsets.append(sub[:])
            return

        # not take
        helper(sub, idx + 1)

        # take
        sub.append(arr[idx])
        helper(sub, idx + 1)

        sub.pop()

    helper([], 0)
    return subsets

subs = get_subsets([1, 2, 3]) 
print(subs)


"""
    TC: O(n* 2^n)
    SC: O(n* 2^n)
"""

