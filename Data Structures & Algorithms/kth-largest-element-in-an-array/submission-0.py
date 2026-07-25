class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k > len(nums):
            return None
        nums = [-s for s in nums]
        heapq.heapify(nums)
        
        while k > 1:
            val = heapq.heappop(nums)
            k -= 1
        val =  -heapq.heappop(nums)
        return val