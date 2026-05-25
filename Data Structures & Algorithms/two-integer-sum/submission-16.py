class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nMap = defaultdict(int)
        for i, n in enumerate(nums):
            find = target - n
            if find in nMap:
                return [nMap[find], i]
            nMap[n] = i