class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        hashset = {}

        for num in nums:
            hashset[num] = 1 + hashset.get(num, 0)
        
        sorted_dict = dict(sorted(hashset.items(), key=lambda x: x[1], reverse=True))

        for key in sorted_dict:
            if(len(output) == k):
                break
            output.append(key)
        
        return output
