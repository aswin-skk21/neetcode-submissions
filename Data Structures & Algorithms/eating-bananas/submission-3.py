class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l <= r:
            mid = l + (r - l) // 2
            if self.check(piles, mid, h) == True:
                r = mid - 1
            else: 
                l = mid + 1 
        return l 

    def check(self, piles: List[int], mid: int, h: int) -> bool: 
        count = 0
        for i in piles: 
            count += (i // mid + 1 if i % mid != 0 else i // mid)
        return count <= h
