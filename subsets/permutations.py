def swap_char(word, i, j):
    swap_index = list(word)
    swap_index[i], swap_index[j] = swap_index[j], swap_index[i]
    return ''.join(swap_index)

def permute_word(s):
    results = []
    def permute_rec(s, c_idx):
        if c_idx == len(s) - 1:
            results.append(s)
            return

        for i in range(c_idx, len(s)):
            s = swap_char(s, c_idx, i)
            permute_rec(s, c_idx + 1)

    permute_rec(s, 0)
    return results

"""
    TC: O(n * n!)
    SC: O(n)
"""
        