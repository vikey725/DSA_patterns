def least_time(tasks, n):
    frequencies = {}
    for t in tasks:
        frequencies[t] = frequencies.get(t, 0) + 1
    
    frequencies = dict(sorted(frequencies.items(), key=lambda x:x[1]))

    max_freq = frequencies.popitem()[1]
    idle_time = (max_freq - 1) * n
    while frequencies and idle_time > 0:
        idle_time -= min(max_freq - 1, frequencies.popitem()[1])
    
    idle_time = max(0, idle_time)

    return idle_time + len(tasks)

"""
    TC: O(n)
    SC: O(1)
"""


