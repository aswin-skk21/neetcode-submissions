class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        track = set()
        l, r = 0, 0
        res = 0
        for r in range(len(s)): 
            while s[r] in track: 
                track.remove(s[l])
                l += 1 
            if s[r] not in track: 
                track.add(s[r])    
            res = max(r - l + 1, res)
        return res