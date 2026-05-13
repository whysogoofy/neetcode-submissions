class TrieNode:
    def __init__(self, val="", isEnd=False):
        self.val = val
        self.isEnd = isEnd
        self.children = [None for _ in range(26)]

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for i, char in enumerate(word):
            child_idx = ord(char) - ord('a')
            
            if not curr.children[child_idx]:
                isEnd = True if (i == len(word) - 1) else False
                curr.children[child_idx] = TrieNode(char, isEnd)
            
            if i == len(word) - 1:
                curr.children[child_idx].isEnd = True

            curr = curr.children[child_idx]

    def search(self, word: str) -> bool:
        curr = self.root

        for i, char in enumerate(word):
            child_idx = ord(char) - ord('a')
            if not curr.children[child_idx]:
                return False
            if (i == len(word) - 1) and not curr.children[child_idx].isEnd:
                return False
            if (i == len(word) -1) and curr.children[child_idx].isEnd:
                return True
            
            curr = curr.children[child_idx]

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for i, char in enumerate(prefix):
            child_idx = ord(char) - ord('a')

            if not curr.children[child_idx]:
                return False
            
            curr = curr.children[child_idx]
        
        return True
        