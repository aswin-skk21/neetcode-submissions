class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))
    def helper(self, nums): 
        prev2 = 0
        prev1 = 0
        for house in nums:
            cur = max(prev1, prev2 + house)
            
            prev2 = prev1
            prev1 = cur
        
        return max(prev1, prev2)