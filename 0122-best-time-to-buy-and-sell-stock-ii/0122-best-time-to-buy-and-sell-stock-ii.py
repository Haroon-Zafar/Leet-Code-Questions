class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Since we can't/haven't made any profit on first day
        profit = 0
        for index in range(1, len(prices)):
            if prices[index] >= prices[index-1]:
                profit += ( prices[index] - prices[index-1] )
        return(profit)
        