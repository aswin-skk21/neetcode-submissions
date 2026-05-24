class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = set()

        for i in range(len(nums)): 

            start, end = i + 1, len(nums) - 1
            target = 0 - nums[i]

            while start < end: 
                curr = nums[start] + nums[end]

                if curr > target: 
                    end -= 1
                elif curr < target: 
                    start += 1
                else:
                    res.add((nums[i], nums[start], nums[end]))
                    start += 1
                    end -= 1
                    
        return [list(elem) for elem in res]