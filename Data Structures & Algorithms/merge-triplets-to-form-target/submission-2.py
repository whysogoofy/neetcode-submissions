class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        match = [0, 0, 0]

        for triplet in triplets:
            if sum(match) == 3:
                break

            a, b, c = triplet
            ta, tb, tc = target
            if a > ta or b > tb or c > tc:
                continue
            if a == ta and not match[0]:
                match[0] = 1
            if b == tb and not match[1]:
                match[1] = 1
            if c == tc and not match[2]:
                match[2] = 1
        
        return sum(match) == 3