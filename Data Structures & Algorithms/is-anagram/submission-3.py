class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashmap = defaultdict(int)

        for i in range(len(s)):
            sc, tc = s[i], t[i]
            hashmap[sc] += 1
            hashmap[tc] -= 1
        
        for val in hashmap.values():
            if val != 0:
                return False
        
        return True