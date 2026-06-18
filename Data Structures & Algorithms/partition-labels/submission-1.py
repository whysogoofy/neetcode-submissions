class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap = [0 for _ in range(26)]
        size, end, output = 0, 0, []

        for i, char in enumerate(s):
            hashmap[ord(char)-ord("a")] = i
        
        for i, char in enumerate(s):
            if hashmap[ord(char)-ord("a")] > end:
                end = hashmap[ord(char)-ord("a")]
            
            size += 1
            if i == end:
                output.append(size)
                size = 0
        
        return output
