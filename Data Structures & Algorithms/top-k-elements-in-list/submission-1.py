class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        hashset = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            hashset[num] = 1 + hashset.get(num, 0)
        
        for key in hashset:
            freq[hashset[key]].append(key)

        for i in range(len(nums), 0, -1):
            for n in freq[i]:
                output.append(n)
                if len(output) == k:
                    return output
        
        return output
