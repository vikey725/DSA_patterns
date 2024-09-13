def sort_colors(colors):
    i, l, r = 0, 0, len(colors) - 1

    while l < r:
        if colors[i] == 0:
            colors[i], colors[l] = colors[l], colors[i]
            l += 1
            i += 1 
        elif colors[i] == 2:
            colors[i], colors[r] = colors[r], colors[i]
            r -= 1
        else:
            i += 1
    
    return colors

"""
    TC: O(n)
    SC: O(1)
"""
