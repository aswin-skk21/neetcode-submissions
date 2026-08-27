class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        f = defaultdict(list)
        distances = defaultdict(int)
        for s, d, p in flights: 
            f[s].append([d, p])
        
        heap = [(0, src, 0)]

        while heap: 
            cost, place, stops = heapq.heappop(heap)
            if place == dst:
                return cost
            if place in distances and distances[place] <= stops:
                continue
            distances[place] = stops
            
            if stops == k + 1: 
                continue 

            for dsts, price in f[place]:
                heapq.heappush(heap, (cost + price, dsts, stops + 1))
            
        return -1 