class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
            
        i1, i2, i3, n, m = 0, 0, 0, 0, 0
        curr = -1

        while i3 < len(s3):
            if i1 < len(s1) and i2 < len(s2) and s3[i3] == s2[i2] and s3[i3] == s1[i1]:
                if curr == 0:
                    i1 += 1
                    i3 += 1
                elif curr == 1:
                    i2 += 1
                    i3 += 1
                else:
                    # tmp1, tmp2, tmp3 = i1, i2, i3
                    i2 += 1
                    i3 += 1
                    curr = 0

            elif i1 < len(s1) and s3[i3] == s1[i1]:
                if curr != 0:
                    n += 1
                    curr = 0
                i1 += 1
                i3 += 1
            elif i2 < len(s2) and s3[i3] == s2[i2]:
                if curr != 1:
                    m += 1
                    curr = 1
                i2 += 1
                i3 += 1
            else:
                return False
        
        return abs(m-n) <= 1
                