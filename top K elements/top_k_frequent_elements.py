from heapq import heappush, heappop, heappushpop
from collections import Counter

def top_k_frequent(arr, k):
    counter = Counter(arr)
    k_frequent = []
    for num, cnt in counter.items():
        if len(k_frequent) < k:
            heappush(k_frequent, (cnt, num))
        else:
            if k_frequent[0][0] <= cnt:
                heappushpop(k_frequent, (cnt, num))

    return [item[1] for item in k_frequent]
