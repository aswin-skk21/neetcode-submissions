class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            root.addWord(word)

        COL, ROW = len(board[0]), len(board)
        res, visited = set(), set()

        def dfs(r, c, node, word):

            if (
                r == ROW
                or c == COL
                or r < 0
                or c < 0
                or board[r][c] not in node.children
                or (r, c) in visited
            ):
                return

            visited.add((r, c))

            node = node.children[board[r][c]]
            word += board[r][c]
            if node.end:
                res.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            visited.remove((r, c))
            
        for r in range(ROW):
            for c in range(COL):
                dfs(r, c, root, "")

        return list(res)
