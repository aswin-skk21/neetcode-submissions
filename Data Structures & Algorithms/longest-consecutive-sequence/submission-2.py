class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n_set = set(nums)
        max = 0 
        for i in range(len(nums)):
            l_max = 0
            num = nums[i]
            if num - 1 in n_set:
                continue
            l_max += 1
            while (num + 1 in n_set):
                num += 1
                l_max += 1
            if l_max > max: 
                max = l_max
        return max