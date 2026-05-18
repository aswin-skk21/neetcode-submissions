class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Dict = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in Dict:
                return [Dict[diff], i]
            Dict[nums[i]] = i