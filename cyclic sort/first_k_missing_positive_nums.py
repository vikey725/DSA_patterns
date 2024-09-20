def first_k_missing_numbers(arr, k):
    n = len(arr)
    i = 0

    while i < n:
        val = arr[i]

        if 1 <= val <= n and arr[val - 1] != val:
            arr[i], arr[val - 1] = arr[val - 1], arr[i]
        else:
            i += 1

    elements_not_at_pos = set()
    for i in range(n):
        
        if arr[i] != i + 1:
            if arr[i] > 0:
                elements_not_at_pos.add(arr[i])

    result = []
    i = 0
    while i < n + k:
        if i < n:
            if arr[i] != i + 1:
                result.append(i + 1)
        else:
            if i + 1 not in elements_not_at_pos:
                result.append(i + 1)
        if len(result) == k:
            break
        i += 1

        

    return result




res = first_k_missing_numbers([-1, 2, -8, -3, 4, 10, 6, 3], 10)
print(res)

"""
    TC: O(n + k)
    SC: O(k)
"""