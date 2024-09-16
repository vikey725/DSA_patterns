# def find_repeated_sequences_basic(dna, k):
#     checker = set()
#     result = set()
#     s = 0
#     for s in range(len(dna) - k + 1):
#         sub = dna[s: s + k]
#         if sub in checker:
#             result.add(sub)
#         else:
#             checker.add(sub)
    
#     return result

# """
#     TC: O(n * k)
#     SC: O(n * k)
# """

def find_repeated_sequences(dna, k):
    n = len(dna)
    mappings = {'A': 1, 'C': 2, 'G': 3, 'T': 4}

    base_val = 4

    numbers = []
    for ch in dna:
        numbers.append(mappings.get(ch))

    hash_val = 0

    checker = set()
    output = set()

    for i in range(n - k + 1):
        if i == 0:
            for j in range(k):
                hash_val += numbers[j] * (base_val ** (k - j - 1))
        
        else:
            prev_hash_val = hash_val
            hash_val = ((prev_hash_val - numbers[i - 1] * (base_val ** (k - 1))) * base_val) + numbers[i + k - 1]

        if hash_val in checker:
            output.add(dna[i: i + k])
        else:
            checker.add(hash_val)

    return output

"""
    TC: O(n) -> avg case O(n * k) -> worst case
    SC: O(n)
"""



