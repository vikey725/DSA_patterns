import heapq


def tasks(tasks_list):
    optimal_machines = 0
    machines_available = []

    # heapify tasks based on start time
    heapq.heapify(tasks_list)

    while tasks_list:
        task = heapq.heappop(tasks_list)

        optimal_machines += 1

        if machines_available and task[0] >= machines_available[0][0]:
            machine_in_use = heapq.heappop(machines_available)
            
            machine_in_use = (task[1], machine_in_use[1])
        else:
            optimal_machines += 1
            machine_in_use = (task[1], optimal_machines)

        heapq.heappush(machines_available, machine_in_use)
    
    return optimal_machines


"""
    TC: O(n * log n)
    SC: O(n)
"""