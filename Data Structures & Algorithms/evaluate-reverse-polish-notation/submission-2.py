class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = ['+', '-', '*', '/']
        stack = []

        for s in tokens:
            # print(stack)
            if s not in operations:
                stack.append(int(s))
            else:
                opnd2 = stack.pop()
                opnd1 = stack.pop()
                if s == '+':
                    stack.append(opnd1 + opnd2)
                elif s == "-":
                    stack.append(opnd1 - opnd2)
                elif s == "*":
                    stack.append(opnd1 * opnd2)
                elif s == "/":
                    stack.append(int(opnd1 / opnd2))
        
        return stack[0]

