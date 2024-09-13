def is_not_cycle(nums, prev_direction, pointer):
    current_child = nums[pointer]
    current_direction = current_child >= 0

    # if prev & current has opposite sign or current_child forms a single node cycle 
    if prev_direction != current_direction or current_child % len(nums) == 0:
        return True
    
    return False 
    

def next_step(pointer, value, size):
    result = (pointer + value) % size
    if result < 0:
        result += size
    return result 

def circular_array_loop(nums):
    size = len(nums)

    for i in range(size):
        slow, fast = i, i
        direction = nums[slow] >= 0

        while True:
            slow = next_step(slow, nums[slow], size)
            if is_not_cycle(nums, direction, slow):
                break

            fast = next_step(fast, nums[fast], size)
            if is_not_cycle(nums, direction, fast):
                break

            fast = next_step(fast, nums[fast], size)
            if is_not_cycle(nums, direction, fast):
                break

            if fast == slow:
                return True
    
    return False


"""
    TC: O(n**2)
    SC: O(1) 
"""

