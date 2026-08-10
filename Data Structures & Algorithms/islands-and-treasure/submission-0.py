class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()
        q = collections.deque()

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    q.append((row, col))
                    visited.add((row, col))

        dist = 0
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = dist
                for r, c in directions:
                    nr, nc = row + r, col + c
                    if (
                        nr < ROWS
                        and nr >= 0
                        and nc < COLS
                        and nc >= 0
                        and (nr, nc) not in visited
                        and grid[nr][nc] != -1
                    ):
                        q.append((nr, nc))
                        visited.add((nr, nc))
            dist += 1
            