from heapq import *

class MedianOfStream:
  def __init__(self):
        self.min_heap = []
        self.max_heap = []

  # This function should take a number and store it
  def insert_num(self, num):
        # Write your code here
        if not self.max_heap or num > -self.max_heap[0]:
            heappush(self.min_heap, num)
        else:
            heappush(self.max_heap, -num)

        if len(self.min_heap) > len(self.max_heap):
            val = heappop(self.min_heap)
            heappush(self.max_heap, -val)
        elif len(self.max_heap) > len(self.min_heap):
            val = heappop(self.max_heap)
            heappush(self.min_heap, -val)  

  # This function should return the median of the stored numbers
  def find_median(self):
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        elif len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return (self.min_heap[0] - self.max_heap[0]) / 2.0
        

# mos = MedianOfStream()
# mos.insert_num(12)
# print(mos.min_heap, mos.max_heap)
# mos.insert_num(46)
# print(mos.min_heap, mos.max_heap)
# mos.insert_num(32)
# print(mos.min_heap, mos.max_heap)
# print(mos.find_median())

"""
    TC: insert_num: O(log n)
    SC: find_median: O(1)
"""