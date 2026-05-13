class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.charMap = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for char in word:
            if not curr.charMap.get(char, None):
                curr.charMap[char] = TrieNode()
        
            curr = curr.charMap[char]
        
        curr.isEnd = True
    
    def search_nested(self, word: str, node: TrieNode) -> bool:
        # if not word:
        #     return True
        # print("nested",word)
        curr = node

        for i, char in enumerate(word):
            if not curr.charMap.get(char, None) and char != '.':
                # print("reason 1", char, word)
                return False
            if char == '.':
                if not len(curr.charMap):
                    # print("reason 2", char, word)
                    return False
                for key in curr.charMap:
                    if self.search_nested(word[i+1:], curr.charMap[key]):
                        return True
                return False
            else:
                curr = curr.charMap[char]

        return True if curr.isEnd else False

    def search(self, word: str) -> bool:
        # if word == "..":
        #     return False
        curr = self.root

        for i, char in enumerate(word):
            if not curr.charMap.get(char, None) and char != '.':
                return False
            if char == '.':
                if not len(curr.charMap):
                    return False
                for key in curr.charMap:
                    if self.search_nested(word[i+1:], curr.charMap[key]):
                        return True
                return False
            else:
                curr = curr.charMap[char]
        
        return True if curr.isEnd else False

        
