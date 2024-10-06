import heapq

def find_kth_largest(nums, k):
    kth_largest = []
    for num in nums:
        if len(kth_largest) < k:
            heapq.heappush(kth_largest, num)
        else:
            heapq.heappushpop(kth_largest, num)
    return kth_largest[0]
