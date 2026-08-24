class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        heap = [[grid[0][0], 0, 0]]
        drc = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visit.add((0, 0))
        
        while heap: 
            t, r, c = heapq.heappop(heap)
            if r == N - 1 and c == N - 1:
                return t
            for dr, dc in drc:
                nR, nC = dr + r, dc + c
                if (nR < 0 or nC < 0 or nR == N or nC == N or (nR, nC) in visit):
                    continue
                visit.add((nR, nC))
                heapq.heappush(heap, [max(t, grid[nR][nC]), nR, nC])
        