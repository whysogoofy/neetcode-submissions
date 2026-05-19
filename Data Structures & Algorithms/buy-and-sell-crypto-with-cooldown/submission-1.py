class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        
        def dfs(i, last, stock):
            if i == len(prices):
                return 0
            if (i, last, stock) in dp:
                return dp[(i, last, stock)]
            
            if stock:
                dp[(i, last, stock)] = max(prices[i] + dfs(i+1, "sell", False), dfs(i+1, "cooldown", True))
                return dp[(i, last, stock)]
            else:
                if last == "sell":
                    dp[(i, last, stock)] = dfs(i+1, "cooldown", False)
                    return dp[(i, last, stock)]
                else:
                    dp[(i, last, stock)] = max(dfs(i+1, "buy", True)-prices[i], dfs(i+1, "cooldown", False))
                    return dp[(i, last, stock)]
            
        return dfs(0, "cooldown", False)
