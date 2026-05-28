class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0 
        res = 0
        freqMap = defaultdict(int)

        for r in range(len(s)):
            freqMap[s[r]] += 1
            while ((r - l + 1) - max(freqMap.values()) > k): 
                freqMap[s[l]] -= 1
                l += 1
            res = max(r - l + 1, res)
        
        return res