class Solution:
    def trap(self, height: List[int]) -> int:
        max_l, max_r, l, r, area = height[0], height[-1], 0, len(height) - 1, 0

        while l < r:
            if max_l <= max_r:
                area += max(0, max_l - height[l])
                l += 1
                max_l = max(max_l, height[l])
            else:
                area += max(0, max_r - height[r])
                r -= 1
                max_r = max(max_r, height[r])
        
        return area