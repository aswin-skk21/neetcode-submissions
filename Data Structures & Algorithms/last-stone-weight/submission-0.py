class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        if not stones:
            return 0

        while len(stones) > 1:
            x, y = -heapq.heappop(stones), -heapq.heappop(stones)
            if x < y:
                y = y - x
                heapq.heappush(stones, -y)
            elif y < x: 
                x = x - y
                heapq.heappush(stones, -x)
        return 0 if not stones else -stones[0]