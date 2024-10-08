def jump_game(nums):
    max_num = 0
    for i in range(len(nums)):
        if i > max_num:
            return False
        
        max_num = max(max_num, i + nums[i])
    return True