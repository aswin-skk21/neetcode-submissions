class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        result = []
        for idx, val in enumerate(nums): 
            find = target - val
            if find in map: 
                result.append(map[find])
                result.append(idx)
                return result
            map[val] = idx

        