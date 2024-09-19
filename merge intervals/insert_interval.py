def insert_interval(existing_intervals, new_interval):
    result = []
    s = 0

    # add all interval from existing intervals whose start is less than ne interval's start
    while s < len(existing_intervals):
        if existing_intervals[s][0] <= new_interval[0]:
            result.append(existing_intervals[s])
            s += 1
        else:
          break
    
    # add new interval to the result or merge it to the last value of result
    if result and result[-1][1] >= new_interval[0]:
      result[-1][1] = max(result[-1][1], new_interval[1])
    else:
      result.append(new_interval)
    
    # merge or add the remaining interval
    while s < len(existing_intervals):
        if result[-1][1] >= existing_intervals[s][0]:
            result[-1][1] = max(result[-1][1], existing_intervals[s][1])
        else:
            result.append(existing_intervals[s])
        s += 1

    return result

"""
    TC: O(n)
    SC: O(n)
"""

