class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        maxArea = 0

        def bfs(r, c):
            area = 0
            queue = deque()
            grid[r][c] = 0
            queue.append((r, c))
            area += 1

            while queue:
                row, col = queue.popleft()
                for r, c in directions:
                    if (
                        row + r < 0
                        or row + r >= ROWS
                        or col + c < 0
                        or col + c >= COLS
                        or grid[row + r][col + c] == 0
                    ):
                        continue
                    queue.append((row + r, col + c))
                    grid[row + r][col + c] = 0
                    area += 1
            return area

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    area = bfs(row, col)
                    maxArea = max(maxArea, area)
        return maxArea
