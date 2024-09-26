from heapq import *

def get_median(max_heap, min_heap, k, medians):
    if (k & 1) == 1:
        medians.append(float(max_heap[0] * -1))
    else:
        medians.append((float(max_heap[0] * -1) + float(min_heap[0])) * 0.5)


def median_sliding_window(nums, k):
    medians = []
    out_num_tracker = {}

    balance = 0
    max_heap, min_heap = [], []

    # insert k numbers into max heap
    for i in range(k):
        heappush(max_heap, -1 * nums[i])

    # insert k//2 numbers into min_heap
    for i in range(k//2):
        heappush(min_heap, -1 * max_heap[0])
        heappop(max_heap)

    # calculate median and insert into medians
    get_median(max_heap, min_heap, k, medians)
    
    for i in range(k, len(nums)):
        out_num = nums[i - k]
        in_num = nums[i] 


        if out_num <= -1 * max_heap[0]:
            # if out_num is in max_heap (-1)
            balance -= 1
        else:
            # if out_num in min_heap (+1)
            balance += 1

        # add out_num to tracker
        out_num_tracker[out_num] = out_num_tracker.get(out_num, 0) + 1

        # add numbers to heap
        if max_heap and in_num <= -1 * max_heap[0]:
            balance += 1
            heappush(max_heap, -1 * in_num)
        else:
            balance -= 1
            heappush(min_heap, in_num)

        # balance the tree
        if balance < 0:
            heappush(max_heap, -1 * min_heap[0])
            heappop(min_heap)
        elif balance > 0:
            heappush(min_heap, -1 * max_heap[0])
            heappop(max_heap)

        balance = 0

        while max_heap and -1 * max_heap[0] in out_num_tracker and out_num_tracker[-1 * max_heap[0]] > 0:
            out_num_tracker[-1 * max_heap[0]] = out_num_tracker[-1 * max_heap[0]] - 1
            heappop(max_heap)

        while min_heap and min_heap[0] in out_num_tracker and out_num_tracker[min_heap[0]] > 0:
            out_num_tracker[min_heap[0]] = out_num_tracker[min_heap[0]] - 1
            heappop(min_heap)

        get_median(max_heap, min_heap, k, medians)
    return medians


"""
    TC: O(n * log n)
    SC: O(n)
"""


        

    

    

nums = [1, 3, -1, 2, -2, -3, 5, 1, 5, 3]
median_sliding_window(nums, 4)