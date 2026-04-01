def max_profit(prices: list[int]) -> int:
    """
    Find the maximum profit from a single buy and sell transaction.
    Args:
        prices: List of stock prices where prices[i] is the price on day i.
    Returns:
        Maximum profit achievable. Returns 0 if no profit is possible.
    """
    price_lowest = prices[0]
    profit_max = 0

    for i in range(len(prices)):        
        if prices[i] < price_lowest:
            price_lowest = prices[i]
        if (prices[i] - price_lowest) > profit_max:
            profit_max = prices[i] - price_lowest

    return profit_max
