class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            if not stack: stack.append(i)

            while stack and temperatures[stack[-1]] < temp:
                output[stack[-1]] = i - stack[-1]
                stack.pop()
            
            stack.append(i)
        
        return output