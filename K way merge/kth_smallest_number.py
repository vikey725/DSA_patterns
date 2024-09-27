from heapq import *


def k_smallest_number(lists, k):
    n = len(lists)
    min_heap = [(lists[i][0], i, 0) for i in range(n) if len(lists[i]) > 0]
    heapify(min_heap)

    merged = []
    smallest_num = 0
    while min_heap:
        smallest_num, i, j = heappop(min_heap)
        merged.append(smallest_num)

        if len(merged) == k:
            break

        if j + 1 < len(lists[i]):
            heappush(min_heap, (lists[i][j + 1], i, j + 1))

    return smallest_num

"""
    TC: O( (m + k) log m)
    SC: O(m)
"""