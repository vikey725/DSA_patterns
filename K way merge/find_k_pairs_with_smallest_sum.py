from heapq import *


def k_smallest_pairs(list1, list2, k):
    min_heap = [(list1[i] + list2[0], i, 0) for i in range(len(list1))]
    heapify(min_heap)

    smallest_pairs = []
    while min_heap:
        _, i, j = heappop(min_heap)
        smallest_pairs.append([list1[i], list2[j]])

        if len(smallest_pairs) == k:
            break

        if j + 1 < len(list2):
            heappush(min_heap, (list1[i] + list2[j + 1], i, j + 1))


    return smallest_pairs