class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freqMap = defaultdict(int)

        for num in nums: 
            freqMap[num] += 1

        arr = [[] for i in range(len(nums) + 1)]

        for val, idx in freqMap.items():
            arr[idx].append(val)
            
        res = []

        index = len(nums)
        count = 0
        while count < k:
            for num in arr[index]:
                res.append(num)
                count += 1
            index -= 1
        return res