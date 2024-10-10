def matchsticks_to_square(matchsticks):
    n = len(matchsticks)
    if n < 4:
        return False
    total = sum(matchsticks)
    if total % 4 != 0:
        return False
    
    side_length = total // 4
    
    if max(matchsticks) > side_length:
        return False
    
    print(total, side_length)
    
    visited = set()
    count = 0
    solved = False
    def solve(i, count):
        if i == 4:
            if len(visited) == n:
                nonlocal solved
                solved = True
            return
            
               
        for j in range(n):
            if j not in visited and count + matchsticks[j] <= side_length:
                visited.add(j)
                count += matchsticks[j]

                if count == side_length:
                    solve(i + 1, 0)

                
                solve(i, count)
                if solved:
                    return 
                visited.remove(j)
                count -= matchsticks[j]
        return False

    solve(0, 0)
    if solved:
      return True
    return False

res = matchsticks_to_square([86,258,129,129,86,129,258,86,129,129,129,516])
print(res)