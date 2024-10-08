def largest_palindrome(num):
    counter = [0 for _ in range(10)]
    for ch in num:
        counter[int(ch)] += 1

    mid_val = None
    first_half = ""
    second_half = ""
    for i in range(9, -1, -1):
        if counter[i] != 0:
            num_times_in_half = counter[i] // 2

            if num_times_in_half != 0:
                first_half = first_half + str(i) * num_times_in_half
                second_half = str(i) * num_times_in_half + second_half
                
            if not mid_val:
                mid_val = None if counter[i] % 2 == 0 else str(i)

    if mid_val:
        res = first_half + mid_val + second_half
    else:
        res = first_half + second_half

    if len(res) > 0 and len(res.strip('0')) == 0:
      return "0"
    
    res = res.strip('0')
    return res


