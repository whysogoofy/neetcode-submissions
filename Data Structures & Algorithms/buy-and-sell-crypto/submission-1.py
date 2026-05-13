class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, i, j = 0, 0, 1
        
        while j < len(prices):
            if prices[j] < prices[i]:
                i = j
                j += 1
            else:
                profit = max(profit, prices[j] - prices[i])
                j += 1
            
        return profit
            

        