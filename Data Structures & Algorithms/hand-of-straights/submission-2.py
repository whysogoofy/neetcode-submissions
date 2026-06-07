class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        hashMap = {}

        for val in hand:
            hashMap[val] = hashMap.get(val, 0) + 1
            
        minHeap = list(hashMap.keys())
        heapq.heapify(minHeap)
        
        grp = []

        while minHeap:
            min_val = minHeap[0]
            
            for i in range(min_val, min_val + groupSize):
                if i not in hashMap:
                    return False
                hashMap[i] -= 1
                if hashMap[i] == 0:
                    if i != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
        
        return True
                    
                