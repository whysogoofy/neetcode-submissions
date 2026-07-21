class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, last_min, last_max = 0, prices[0], prices[0]

        for p in prices:
            last_max = max(last_max, p)
            if p < last_max or p < last_min:
                profit += last_max - last_min
                last_max, last_min = p, p
        
        return profit if last_min == last_max else profit + last_max - last_min

        