class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []

        def dfs(open_p, close_p, current_str):
            # Base case: string is complete
            if len(current_str) == 2 * n:
                output.append(current_str)
                return

            # Try adding an opening bracket
            if open_p < n:
                dfs(open_p + 1, close_p, current_str + "(")

            # Try adding a closing bracket (only if it doesn't break validity)
            if close_p < open_p:
                dfs(open_p, close_p + 1, current_str + ")")

        dfs(0, 0, "")
        return output