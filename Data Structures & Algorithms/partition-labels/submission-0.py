class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap, res = defaultdict(int), [1]
        curr = set([s[0]])
        hashmap[s[0]] = 0

        for i in range(1, len(s)):
            char = s[i]
            hashmap[char] += 1
        
        for i in range(1, len(s)):
            char = s[i]
            # print(char, curr, res, hashmap)
            check = False
            for key in curr:
                if hashmap[key]:
                    res[-1] += 1
                    check = True
                    curr.add(char)
                    break
            if not check:
                res.append(1)
                curr = set([s[i]])
            hashmap[char] -= 1
        
        return res