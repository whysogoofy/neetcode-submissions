class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool: 
        cache = set()
 
        def dfs(i1, i2):
            i3 = i1+i2
            if i3 == len(s3):
                return (i1 == len(s1)) and (i2 == len(s2))
            if (i1, i2) in cache:
                return False

            if i1 < len(s1) and s1[i1] == s3[i3]:
                if dfs(i1 + 1, i2):
                    return True
            
            if i2 < len(s2) and s2[i2] == s3[i3]:
                if dfs(i1, i2 + 1):
                    return True
            
            cache.add((i1, i2))
            return False
                    
    
        return dfs(0, 0)
        

                    


                