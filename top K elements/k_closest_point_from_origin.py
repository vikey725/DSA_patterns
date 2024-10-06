import heapq

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def k_closest(points, k):
    closest_heap = []
    for idx, point in enumerate(points):
        d = (point.x * point.x + point.y * point.y)
        
        if idx < k:
            heapq.heappush(closest_heap, (-d, point))
        else:
            if d < -1 * closest_heap[0][0]:
                heapq.heappushpop(closest_heap, (-d, point))
    
    return [item[1] for item in closest_heap]