class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        matched_indices = set()
        ta, tb, tc = target

        for a, b, c in triplets:
            if a > ta or b > tb or c > tc:
                continue

            if a == ta:
                matched_indices.add(0)
            if b == tb:
                matched_indices.add(1)
            if c == tc:
                matched_indices.add(2)
            
            if len(matched_indices) == 3:
                return True
        
        return len(matched_indices) == 3