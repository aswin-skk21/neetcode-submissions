class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()

        def dfs(r, c, visited):
            if (r == ROWS or c == COLS or r < 0 or c < 0 or board[r][c] == 'X'):
                return 
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if (nr, nc) not in visited:
                    dfs(nr, nc, visited)

        for row in range(ROWS):
            if (row, COLS -1) not in visited:
                dfs(row, COLS - 1, visited)
            if (row, 0) not in visited:
                dfs(row, 0, visited)
                

        for col in range(COLS):
            if (0, col) not in visited:
                dfs(0, col, visited)
            if (ROWS - 1, col) not in visited:
                dfs(ROWS - 1, col, visited)
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited:
                    board[r][c] = 'X'
                    