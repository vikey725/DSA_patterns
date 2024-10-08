def jump_game_two(nums):
    l, r = 0, 0
    cnt = 0
    len_nums = len(nums)
    while r < (len_nums - 1):
        farthest = 0
        for k in range(l, r + 1):
            farthest = max(farthest, k + nums[k])
        l, r = r + 1, farthest
        cnt += 1
    return cnt
