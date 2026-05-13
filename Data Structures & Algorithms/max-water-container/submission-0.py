class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0

        for i in range(len(heights) - 1):
            for j in range(i + 1, len(heights)):
                area = (j - i) * (max(heights[i], heights[j]) - abs(heights[i] - heights[j]))
                if area > maxArea:
                    maxArea = area
        
        return maxArea