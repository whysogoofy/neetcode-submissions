class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first, second = cost[-2], cost[-1]
        
        for i in range(len(cost)-3, -1, -1):
            tmp = first
            first = cost[i] + min(first, second)
            second = tmp
        
        return min(first, second)