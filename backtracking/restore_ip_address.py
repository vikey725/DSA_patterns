def restore_ip_addresses(s):
    results = []
    n = len(s)

    def is_valid(substr):
        if not substr or len(substr) > 3:
            return False
        
        if substr[0] == '0' and len(substr) > 1:
            return False
        
        if not 0 <= int(substr) <= 255:
            return False 
        
        return True

    def solve(idx, result):
        if len(result) > 4:
            return
        if idx == n:
            if len(result) == 4:
                results.append(".".join(result))
                # print(result)
            return
        
            
        for j in range(idx + 1, idx + 4):
            if not is_valid(s[idx: j]):
                continue
            result.append(s[idx: j])
            # print("res: ", s[idx: j])
            solve(j, result)
        
            result.pop()

    solve(0, [])
    return results