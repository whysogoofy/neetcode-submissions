class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashset = {}
        output = []

        for i, str_e in enumerate(strs):
            s = "".join(sorted(str_e))
            arr_s = [str_e]

            if(hashset.get(s, 0) == 1):
                continue
            hashset[s] = 1

            for j in range(i+1, len(strs)):
                if("".join(sorted(strs[j])) == s):
                    arr_s.append(strs[j])
            
            output.append(arr_s)
        
        return output
