class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        permutations = self.permute(nums[1:])
        output = []

        for p in permutations:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                output.append(p_copy)
            
        return output