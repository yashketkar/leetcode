class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit, min_price = 0, float('inf')
        for i in range(len(prices)):
            min_price = prices[i] if prices[i]<min_price else min_price
            if i>0 and prices[i]<=prices[i-1]:
                continue
            max_profit = prices[i] - min_price if ((prices[i] - min_price) > max_profit) else max_profit
        return max_profit
