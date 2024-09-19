import heapq

def find_sets(intervals):
    intervals.sort(key=lambda x: x[0])

    heap = []
    heapq.heappush(heap, intervals[0][1])

    for i in range(1, len(intervals)):
        # push to heap if min of heap is greater than start of current interval
        if intervals[i][0] < heap[0]:
            heapq.heappush(heap, intervals[i][1])
        else:
            # remove min and add end of current interval
            heapq.heappushpop(heap, intervals[i][1])

    return len(heap)

"""
    TC: O(nlogn)
    SC: O(n)
"""
