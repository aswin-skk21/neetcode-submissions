class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)    
        for n in nums:   
            count[n] += 1
        
        arr = [[] for i in range(len(nums) + 1)]

        for val in count: 
            arr[count[val]].append(val)
        
        result = []
        for i in range(len(arr) - 1, 0, -1):
            if len(arr[i]) == 0: 
                continue
            for j in arr[i]:
                result.append(j)
                if len(result) == k:
                    return result