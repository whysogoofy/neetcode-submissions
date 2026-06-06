class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i in range(len(gas)):
            tank = 0
            j = 0
            while j < len(gas):
                index = (i+j) % len(gas)
                if tank + gas[index] < cost[index]:
                    break
                tank += gas[index] - cost[index]
                j += 1

            if j == len(gas):
                return i

        return -1
                