class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        maxProfit = 0
        currentBuy = prices[0]

        for price in prices:
            if price < currentBuy:
                currentBuy = price
            else:
                currentProfit = price - currentBuy
                maxProfit = max(maxProfit, currentProfit)

        return maxProfit