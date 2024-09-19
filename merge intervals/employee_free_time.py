class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.closed = True

# def employee_free_time(schedule):
#     flattened = [interval for employee in schedule for interval in employee]
#     flattened.sort(key = lambda x: x.start)

#     merged = []
#     for i in range(len(flattened)):
#         if not merged or merged[-1].end < flattened[i].start:
#             merged.append(flattened[i])
#         else:
#             merged[-1].end = max(merged[-1].end, flattened[i].end)

#     free_time = []
#     for i in range(1, len(merged)):
#         if merged[i].start > merged[i-1].end:
#             free_time.append(Interval(merged[i-1].end, merged[i].start))

#     return free_time


# """
#     TC: O(n * log n) => n: count of all intervals in all imployees 
#     SC: O(n)
# """



import heapq 

def employee_free_time(schedule):
    heap = []

    for i in range(schedule):
        heapq.heappush(heap, (schedule[i][0].start, i, 0))

    free_time = []
    if not heap:
        return free_time

    _, i, j = heapq.heappop(heap)
    prev = schedule[i][j].end

    if j + 1 < len(schedule[i]):
        heapq.heappush(heap, schedule[i][j + 1].start, i, j + 1)

    while heap:
        _, i, j = heapq.heappop(heap)
        cur = schedule[i][j]

        if cur.start > prev:
            free_time.append(Interval(prev, cur.start))

        prev = max(prev, cur.end)


        if j + 1 < len(schedule[i]):
            heapq.heappush(heap, schedule[i][j + 1].start, i, j + 1)

    return free_time

"""
    TC: O(m * log n) => n: count of all intervals in all employees and m: no of employees
    SC: O(m)
"""


    
