class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(r, c, visit, prevHeight):
            if (
                (r, c) in visit
                or r == ROWS
                or c == COLS
                or r < 0
                or c < 0
                or heights[r][c] < prevHeight
            ):
                return
            visit.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, visit, heights[r][c])

        for c in range(COLS):
            dfs(ROWS -  1, c, atl, heights[ROWS - 1][c])
            dfs(0, c, pac, heights[0][c])
    
        for r in range(ROWS):
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])
            dfs(r, 0, pac, heights[r][0])
        
        res = []

        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) in pac and (row, col) in atl:
                    res.append([row, col])

        return res