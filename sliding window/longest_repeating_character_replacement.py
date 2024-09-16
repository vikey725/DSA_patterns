def longest_repeating_character_replacement(s, k):
    state = {}
    start = 0
    max_freq = 0
    len_longest_sub = 0

    for end in range(len(s)):
        state[s[end]] = state.get(s[end], 0) + 1
        max_freq = max(max_freq, state[s[end]])

        while max_freq + k < end - start + 1:
            state[s[start]] -= 1
            start += 1
        
        len_longest_sub = max(len_longest_sub, end - start + 1)
    
    return len_longest_sub

"""
    TC: O(n)
    SC: O(1) -> will be storing at max 26 chars
"""