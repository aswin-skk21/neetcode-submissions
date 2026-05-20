class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        pre = [1] * len(nums)
        for i in range(1, len(nums)):
            pre[i] = pre[i - 1] * nums[i - 1]

        s = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            s[i] = s[i + 1] * nums[i + 1]
        
        for i in range(len(nums)):
            res.append(s[i] * pre[i])
        

        return res
        