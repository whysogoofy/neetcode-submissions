class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i in range(len(heights)):
            # stack.append(i)

            # if len(stack) < 2: continue
            prev_index = -1
            # print([i, heights[i]], stack)
            while stack and stack[-1][1] > heights[i]:
                # print((i - stack[-1][0]) * heights[stack[-1][0]])
                max_area = max(max_area, (i - stack[-1][0]) * stack[-1][1])
                prev_index = stack[-1][0]
                stack.pop()

            # print(stack)
            
            if prev_index == -1:
                stack.append([i, heights[i]])
            else:
                stack.append([prev_index, heights[i]]) 
            # print(stack)


        # print(stack)
        while stack:
            # print((len(heights) - stack[-1][0]) * stack[-1][1], len(heights) - stack[-1][0], stack[-1][1])
            # if 
            max_area = max(max_area, (len(heights) - stack[-1][0]) * stack[-1][1])
            # prev_index = stack[-1][0]
            stack.pop()

        return max_area