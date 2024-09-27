from heapq import *

def kth_smallest_element(matrix, k):
    min_heap = [(matrix[i][0], i, 0) for i in range(len(matrix))]
    heapify(min_heap)

    combined = []
    smallest_element = 0
    while min_heap:
        smallest_element, i, j = heappop(min_heap)

        combined.append(smallest_element)

        if len(combined) == k:
            break

        if j + 1 < len(matrix[i]):
            heappush(min_heap, (matrix[i][j + 1], i, j + 1))
    
    return smallest_element

"""
    TC: O((min(n,k)+k) × log(min(n,k)))
    SC: O(n)
"""