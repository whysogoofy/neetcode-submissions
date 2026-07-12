from typing import List

class TrieNode:
    def __init__(self, val="", isEnd=False):
        self.val = val
        self.children = {}
        self.isEnd = isEnd
        

class Solution:
    def longestCommonPrefix(self, strs: List[int]) -> str:
        if not strs or "" in strs:
            return ""

        root = TrieNode()

        # Build the Trie
        for st in strs:
            node = root
            for ch in st:
                if ch not in node.children:
                    node.children[ch] = TrieNode(ch)
                node = node.children[ch]
            node.isEnd = True
        
        curr = root
        res = ""

        while not curr.isEnd:
            if len(curr.children) != 1:
                break
            
            key = list(curr.children.keys())[0]
            curr = curr.children[key]
            res += curr.val
        
        return res