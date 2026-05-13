class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = {}

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        head = TrieNode()
        
        for word in wordDict:
            curr = head
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.isEnd = True

        dp = {len(s): True}

        for i in range(len(s) - 1, -1, -1):
            curr = head
            dp[i] = False
            
            for j in range(i, len(s)):
                char = s[j]
                if char not in curr.children:
                    break
                
                curr = curr.children[char]
                
                if curr.isEnd:
                    if dp.get(j + 1, False):
                        dp[i] = True
                        break
            
        return dp[0]