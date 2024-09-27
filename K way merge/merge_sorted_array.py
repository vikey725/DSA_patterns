def merge_sorted(nums1, m, nums2, n):
    i, j, k = m - 1, n - 1, m + n - 1
    while i >= 0 and j >= 0:
        if nums1[i] <= nums2[j]:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        else:
            nums1[k], nums1[i] = nums1[i], nums1[k]
            i -= 1
            k -= 1

    if j >= 0:
        for l in range(j + 1):
            nums1[l] = nums2[l]
    
    return nums1

"""
    TC: O(m + n)
    SC: O(1)
"""