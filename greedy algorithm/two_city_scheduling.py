def two_city_scheduling(costs):
    costs.sort(key = lambda x: x[0] - x[1])

    left, right = 0, len(costs) - 1
    total_cost = 0
    while left < right:
        total_cost = total_cost + costs[left][0] + costs[right][1]
        left += 1
        right -= 1
    
    return total_cost
