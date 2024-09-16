def min_window(str1, str2):
    n, m = len(str1), len(str2)
    idx_s1, idx_s2 = 0, 0
    min_window_len = float('inf')
    min_window_sub = ""

    while idx_s1 < n:
        if str1[idx_s1] == str2[idx_s2]:
            idx_s2 += 1
            if idx_s2 == m:
                s, e = idx_s1, idx_s1
                idx_s2 -= 1 

                while idx_s2 >= 0:
                    if str1[s] == str2[idx_s2]:
                        idx_s2 -= 1
                    s -= 1
                s += 1

                if e - s + 1 < min_window_len:
                    min_window_len = e - s + 1
                    min_window_sub = str1[s: e + 1]
                    

                idx_s2 = 0
                idx_s1 = s
        idx_s1 += 1
        
    return min_window_sub

"""
    TC: O(n * m)
    SC: O(1)
"""