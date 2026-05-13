class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        output = []

        subset = []
        def dfs(i, total):
            if total == target:
                output.append(subset.copy())
                return
            if total > target or i == len(candidates):
                return
            
            subset.append(candidates[i])
            total += candidates[i]
            dfs(i + 1, total)

            subset.pop()
            total -= candidates[i]
            tmp = candidates[i]
            while i < len(candidates) and tmp == candidates[i]:
                i += 1
            dfs(i, total)

        dfs(0, 0)
            
        return output

                
