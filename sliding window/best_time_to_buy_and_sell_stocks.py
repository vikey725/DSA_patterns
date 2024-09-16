def max_profit(prices):
    cur_min = prices[0]
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > cur_min:
            profit = max(profit, prices[i] - cur_min)
        else:
            cur_min = prices[i]
    
    return profit
            