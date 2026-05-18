class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Dict = {}

        for i in range(len(nums)):
            Dict[nums[i]] = i

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in Dict:
                if i != Dict[diff]:
                     return [i, Dict[diff]]