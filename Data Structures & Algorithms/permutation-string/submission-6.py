class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        map_s1 = [0] * 26
        map_s2 = [0] * 26
        matches = 0

        for char in s1:
            map_s1[ord(char) - ord('a')] += 1

        # print(map_s1)
        
        i = 0
        j = len(s1) - 1

        for k in range(0, len(s1)):
            map_s2[ord(s2[k]) - ord('a')] += 1

        for k in range(26):
            if map_s1[k] == map_s2[k]:
                matches += 1
        
        if matches == 26:
            # print("catch")
            return True

        while j < len(s2):
            # print(i, j, matches, map_s2)
            if map_s2[ord(s2[i]) - ord('a')] - 1 == map_s1[ord(s2[i]) - ord('a')]:
                matches += 1
            else:
                if map_s2[ord(s2[i]) - ord('a')] == map_s1[ord(s2[i]) - ord('a')]:
                    matches -= 1
            map_s2[ord(s2[i]) - ord('a')] -= 1
            i += 1
           
            if j == len(s2) - 1:
                if matches == 26:
                    return True
                break

            if map_s2[ord(s2[j+1]) - ord('a')] + 1 == map_s1[ord(s2[j+1]) - ord('a')]:
                matches += 1
            else:
                if map_s2[ord(s2[j+1]) - ord('a')] == map_s1[ord(s2[j+1]) - ord('a')]:
                    matches -= 1
            map_s2[ord(s2[j + 1]) - ord('a')] += 1
            j += 1

            if matches == 26:
                # print("catch")
                return True

        return False



        
        

        