def find_longest_substring(input_str):
    state = {}

    s, e = 0, 0
    n = len(input_str)
    max_sub_len = 0

    while e < n:
        if input_str[e] in state:
            s = max(s, state[input_str[e]] + 1)

        state[input_str[e]] = e

        max_sub_len = max(max_sub_len, e - s + 1)

        e += 1


    return max_sub_len