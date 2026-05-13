class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashset = {}

        for i in range(len(numbers)):
            prev = hashset.get(numbers[i], -1)
            if prev != -1:
                return [prev + 1, i + 1]
            else:
                hashset[target - numbers[i]] = i
        