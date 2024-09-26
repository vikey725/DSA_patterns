# from heapq import *

# def maximum_capital(c, k, capitals, profits):
#     n = len(capitals)
#     combined = sorted(zip(capitals, profits))
    
#     heap = []
#     i = 0
#     while i < n + 1:
#         if k == 0:
#             break
#         # logic 
#         capital = float('inf')
#         if i < n:
#             capital = combined[i][0]
            
#         if capital <= c:
#             heappush(heap, (-combined[i][1], capital))
#             i += 1
#         else:
#             while heap and capital > c and k > 0:
#                 profit, capital = heappop(heap)
#                 profit = -profit
#                 c = c + profit
#                 k -= 1
#             if not heap and capital > c:
#                 break
#     return c

# """
#     TC: O(n * log n)
#     SC: O(n)
# """


from heapq import *

def maximum_capital(c, k, capitals, profits):
    capital_min_heap = []
    profits_max_heap = []
    n = len(capitals)

    for i in range(n):
        heappush(capital_min_heap, (capitals[i], i))

    for _ in range(k):
        while capital_min_heap and capital_min_heap[0] <= c:
            _, idx = heappop(capital_min_heap)
            heappush(profits_max_heap, (-profits[idx]))
    
        if not profits_max_heap:
            break

        profit = heappop(profits_max_heap)
        c += (-profit)

    return c


"""
    TC: O(n * log n)
    SC: O(n)
"""
