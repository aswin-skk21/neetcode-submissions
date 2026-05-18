class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeroCount = 0
        for num in nums: 
            if num == 0:
                zeroCount += 1
            else: 
                product *= num 
        
        if zeroCount > 1:
            return [0] * len(nums)
            
        result = [int(product)] * len(nums)

        for i in range(len(nums)):
            if zeroCount == 1:
                result[i] = 0 if nums[i] else product
            else:
                result[i] = int(result[i]) // int(nums[i])
    
        return result