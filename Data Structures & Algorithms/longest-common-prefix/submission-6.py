class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first=strs[0]
        last=strs[-1]
        l=min(len(first), len(last))
        res=""
        for i in range(l):
            if first[i]==last[i]:
                res+=first[i]
            else:
                break
        return res