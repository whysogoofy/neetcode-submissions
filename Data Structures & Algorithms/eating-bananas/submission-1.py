class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_p, output = max(piles), float("infinity")
        
        l, r = 1, max_p

        while l <= r:
            h_taken = 0 
            mid = (l + r) // 2
            # print(mid, mid, l, r, l+r)

            for pile in piles:
                # print("pile", pile//mid)
                h_taken += pile//mid if pile % mid == 0 else (pile//mid + 1)

            # print(h_taken)
            
            if h_taken <= h:
                output = min(output, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return output