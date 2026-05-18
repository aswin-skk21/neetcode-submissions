class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        for index, val in enumerate(nums):
            search = target - val
            if search in numMap:
                return [numMap[search], index]
            numMap[val] = index
            
