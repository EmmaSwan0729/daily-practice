def max_profit(prices: list[int]) -> int:
    profits = []
    for i in prices:
        for j in profits:
            if prices[j]>prices[i] and j>i:
                profits.append(prices[j])
            else:
                break
    max_profit_value = max(profits)
    return max_profit_value
