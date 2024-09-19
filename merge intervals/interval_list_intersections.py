def intervals_intersection(interval_list_a, interval_list_b):
    
    # Replace this placeholder return statement with your code
    i, j = 0, 0
    m, n = len(interval_list_a), len(interval_list_b)

    intersections = []
    while i < m and j < n:
        start = max(interval_list_a[i][0], interval_list_b[j][0])
        end = min(interval_list_a[i][1], interval_list_b[j][1])

        if start <= end:
            intersections.append([start, end])

        if interval_list_a[i][1] < interval_list_b[j][1]:
            i += 1
        else:
            j += 1

    return intersections

"""
    TC: O(m + n)
    SC: O(m + n)
"""