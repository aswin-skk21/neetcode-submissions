class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCount = 0
        sum = 1
        for i in range(len(nums)):
            if(nums[i] == 0):
                zeroCount += 1
                continue
            sum *= nums[i]
        
        res = []
        if zeroCount == 0:
            for i in range(len(nums)):
                res.append(sum // nums[i])
            
        if zeroCount == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    res.append(sum)
                else: 
                    res.append(0)

        if zeroCount > 1:
            for i in range(len(nums)):
                res.append(0)
        
        return res
        