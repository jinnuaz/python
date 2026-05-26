
prices = [7,1,5,3,6,4]
def maxProfit(prices):

    left        = 0  # left     = buy
    right       = 1  # right    = sell
    maxProfit   = 0

    while (right < len(prices)):
        # Profitable
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            maxProfit = max(maxProfit, profit)
        else:
            left = right

        right = right + 1
    return maxProfit

print(maxProfit(prices))