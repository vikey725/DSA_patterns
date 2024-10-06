import heapq

class KthLargest:
    # Constructor to initialize heap and add values in it
    def __init__(self, k, nums):
        self.k = k
        self.min_heap = []
        for num in nums:
            self.add(num)

    # Adds element in the heap and return the Kth largest
    def add(self, val):
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        elif val > self.min_heap[0]:
            heapq.heappushpop(self.min_heap, val)
        

        return self.min_heap[0]