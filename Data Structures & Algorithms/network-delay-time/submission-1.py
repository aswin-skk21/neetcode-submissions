class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for e in times: 
            edges[e[0]].append([e[2], e[1]])
        
        visited = set()
        minHeap = [(0, k)]
        time = 0

        while minHeap: 
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            time = w1

            for w2, n2 in edges[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (w1 + w2, n2))
        return time if len(visited) == n else -1

