import heapq

def min_refuel_stops(target, start_fuel, stations): 
    if start_fuel >= target:
        return 0
    
    max_heap = []
    i = 0

    station_count = 0
    total_dist = start_fuel
    while total_dist < target:
        if i < len(stations) and stations[i][0] <= total_dist:
            heapq.heappush(max_heap, -1 * stations[i][1])
            i += 1
        elif not max_heap:
            return -1
        else:
            station_count += 1
            fuel = -1 * heapq.heappop(max_heap)
            total_dist += fuel
    if total_dist >= target:
      return station_count
        
    return -1