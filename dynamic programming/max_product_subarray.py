def max_product(nums):
    n = len(nums)

    max_prod = - float('inf')
    prefix, suffix = 1, 1

    for i in range(n):
        prefix *= nums[i]
        suffix *= nums[n - i - 1]

        max_prod = max(max_prod, prefix, suffix)

        if prefix == 0:
            prefix = 1
        if suffix == 0:
            suffix = 1
    return max_prod