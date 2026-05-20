class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sum = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j: 
                    continue
                sum[i] *= nums[j]
        return sum