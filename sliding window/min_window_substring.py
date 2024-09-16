from copy import copy

def min_window(s, t):
    count_dict = {}
    for ch in t:
        count_dict[ch] = count_dict.get(ch, 0) + 1
    
    start, end = 0, 0
    n = len(s)
    min_len = float('inf')
    min_len_str = ''

    while end < n:
        if s[end] in count_dict:
            t_count_dict = copy(count_dict)
            while end < n and t_count_dict != {}:
                if s[end] in t_count_dict:
                    t_count_dict[s[end]] -= 1
                    if t_count_dict[s[end]] == 0:
                        del t_count_dict[s[end]]
                
                if t_count_dict != {}:
                    end += 1

            if t_count_dict == {}:
                # while loop
                t_count_dict = copy(count_dict)
                n_start = end
                while t_count_dict != {}:
                    if s[n_start] in t_count_dict:
                        t_count_dict[s[n_start]] -= 1
                        if t_count_dict[s[n_start]] == 0:
                            del t_count_dict[s[n_start]]
                    if t_count_dict != {}:
                        n_start -= 1
                    else:
                        if min_len > end - n_start + 1:
                            min_len = end - n_start + 1
                            min_len_str = s[n_start: end + 1]

                start = n_start + 1
                end = n_start
            
        end += 1
    return min_len_str

def min_window(s, t):
    req_count = {}
    for ch in t:
        req_count[ch] = req_count.get(ch, 0) + 1

    window = {ch: 0 for ch in req_count.keys()}

    start, end = float('inf'), float('inf')

    l, r = 0, 0
    required = len(req_count)
    current = 0

    while r < len(s):
        if s[r] in req_count:
            window[s[r]] += 1

            if window[s[r]] == req_count[s[r]]:
                current += 1

                if current == required:
                    n_start, n_end = l, r
                    while current == required:
                        if s[l] in req_count:
                            window[s[l]] -= 1

                            if window[s[l]] != req_count[s[l]]:
                                current -= 1
                                break
                        n_start = l
                        l += 1
                    
                    if end - start > n_end - n_start:
                        end, start = n_end, n_start

    if start == float('inf') or end == float('inf'):
        return ""

    return s[start: end + 1]

"""
    TC: O(n + m)
    SC: O(1)
"""
                    

                    


        






