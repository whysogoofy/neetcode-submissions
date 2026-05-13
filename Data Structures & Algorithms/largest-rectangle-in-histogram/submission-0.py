class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0

        for i in range(len(heights)):
            area = 0
            j = i
            k = i

            while j < len(heights) and heights[j] >= heights[i]:
                area += heights[i]
                j += 1
            
            while k >= 0 and heights[k] >= heights[i]:
                if k == i: 
                    k -= 1
                    continue
                area += heights[i]
                k -= 1

            maxArea = max(maxArea, area)
            # print(i, area)
        
        return maxArea