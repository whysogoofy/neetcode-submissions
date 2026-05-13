class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sl = len(s)
        tl = len(t)

        if(sl != tl):
            return False
        
        h_len = 26
        hs = [0] * h_len
        ht = [0] * h_len

        for char_s in s:
            hs[ord(char_s) % h_len] += 1
        
        for char_t in t:
            ht[ord(char_t) % h_len] += 1
        
        if(hs == ht):
            return True
        else:
            return False