def gas_station_journey(gas, cost):
    n = len(gas)
    differences = [gas[i] - cost[i] for i in range(n)] * 2

    start, end = 0, 0
    
    total = 0
    while end < 2 * n:
        total += differences[end]

        if total < 0:
            start = end + 1
            total = 0
        else:
            if end - start + 1 == n:
                return start
        end += 1
    return -1
        

