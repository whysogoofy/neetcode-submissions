class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        max_area, i, j = 0, 0, len(height) - 1

        while i < len(height) and height[i] < height[i + 1]:
            i += 1
        while j > 0 and height[j] < height[j - 1]:
            j -= 1

        while i < j:
            max_area_ele = 0
            max_ele = i + 1
            for k in range(i + 1, j + 1):
                if height[k] > height[max_ele]:
                    max_ele = k
                if height[max_ele] > height[i]:
                    break
            
            for k in range(i+1, max_ele):
                min_h = min(height[max_ele], height[i])
                max_area_ele += min_h - height[k]
            
            max_area += max_area_ele
            i = max_ele
        
        return max_area
                