class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l <= r:
            mid = l + (r - l) // 2
            count = 0
            for i in piles: 
                count += (i // mid + 1 if i % mid != 0 else i // mid)
            if count <= h:
                r = mid - 1
            else: 
                l = mid + 1 
        return l 

        
