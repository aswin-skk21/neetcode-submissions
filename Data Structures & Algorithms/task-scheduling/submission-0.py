class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)

        maxHeap = [-count for count in freq.values()]
        heapq.heapify(maxHeap)
        
        q = deque()
        time = 0

        while maxHeap or q:
            time += 1 
            if maxHeap: 
                val = 1 + heapq.heappop(maxHeap)
                if val != 0:
                    q.append([val, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time