class Solution:
    def maxScore(self, s: str) -> int:
        right1s = s.count("1")
        left0s = 0
        maxScore = 0 

        for i in range(len(s) - 1):
            if s[i] == '0':
                left0s += 1
            else: 
                right1s -= 1
            maxScore = max(left0s + right1s, maxScore)
        
        return maxScore