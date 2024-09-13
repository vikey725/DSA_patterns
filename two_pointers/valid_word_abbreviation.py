def valid_word_abbreviation(word, abbr):
    """
    
    """
    i, j, num = 0, 0, 0
    while i < len(word) and j < len(abbr):
        if abbr[j].isalpha():
            if word[i] != abbr[j]:
                return False
            j += 1
            i += 1
        else:
            if abbr[j] == 0:
                return False
            
            num = 0
            while j < len(abbr) and abbr[j].isdigit():
                num = num * 10 + int(abbr[j])
                j += 1

            i += num

    if i != len(word) or j != len(abbr):
        return False
    
    return True

"""
    TC: O(n) -> n is len of abbreviation
    SC: O(1)
"""

