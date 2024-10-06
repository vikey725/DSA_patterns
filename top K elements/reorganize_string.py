from collections import Counter
import heapq

def reorganize_string(str):
    counter = Counter(str)

    max_heap = []
    for ch, cnt in counter.items():
        max_heap.append((-cnt, ch))

    heapq.heapify(max_heap)

    prev = None
    res = ""
    while max_heap or prev:
        if prev and len(max_heap) == 0:
          return ""
        
        cnt, ch = heapq.heappop(max_heap)
        res += ch
        cnt += 1

        if prev:
            heapq.heappush(max_heap, prev)
            prev = None

        if cnt != 0:
            prev = (cnt, ch)

    return res