class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for st in strs:
            key = "".join(sorted(st))
            arr = hashmap.get(key, [])
            arr.append(st)
            hashmap[key] = arr
        
        return list(hashmap.values())