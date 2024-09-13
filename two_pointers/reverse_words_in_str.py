import re

def reverse_part(char_arr, s, e):
    while s < e:
        char_arr[s], char_arr[e] = char_arr[e], char_arr[s]
        s += 1
        e -= 1

def reverse_words(sentence):
    sentence = re.sub(' +', ' ', sentence.strip())

    char_arr = list(sentence)
    n = len(char_arr)

    # reverse entire arr
    reverse_part(char_arr, 0, n - 1)

    s = 0
    e = 0
    while e <= n:
        if e == n:
            reverse_part(char_arr, s, e - 1)
            break

        if char_arr[e] == ' ':
            reverse_part(char_arr, s, e - 1)
            s = e + 1

    return " ".join(char_arr)

"""
    TC: O(n)
    SC: O(n)
"""


