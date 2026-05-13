class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        root = TrieNode()
        output = []

        for word in words:
            curr = root
            for char in word:
                if not curr.children.get(char, None):
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.isEnd = True
        
        # print(root.children)

        def backtrack(r, c, comb, currNode, currWord):
            # print(currWord)
            if r < 0 or c < 0 or r == ROWS or c == COLS or comb[r][c] == '#':
                return
            if not currNode.children.get(comb[r][c], None):
                return
            if currNode.children[comb[r][c]].isEnd:
                # print("curr word", currWord)
                passWord = currWord + comb[r][c]
                if passWord not in output:
                    output.append(passWord)

            tmpNode = currNode
            currNode = currNode.children[comb[r][c]]
            tmp = comb[r][c]
            # print(tmp, currWord)
            comb[r][c] = '#'

            backtrack(r, c+1, comb, currNode, currWord + tmp)
            backtrack(r, c-1, comb, currNode, currWord + tmp)
            backtrack(r+1, c, comb, currNode, currWord + tmp)
            backtrack(r-1, c, comb, currNode, currWord + tmp)

            currNode = tmpNode
            comb[r][c] = tmp
        
        currPass = root
        for i in range(ROWS):
            for j in range(COLS):
                backtrack(i, j, board, currPass, "")

        return output