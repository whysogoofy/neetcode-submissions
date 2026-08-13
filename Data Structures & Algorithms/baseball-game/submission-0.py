class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            match op:
                case "+":
                    stack.append(int(stack[-1]) + int(stack[-2]))
                case "C":
                    stack.pop()
                case "D":
                    stack.append(int(stack[-1])*2)
                case _:
                    stack.append(int(op))

        return sum(stack)
        