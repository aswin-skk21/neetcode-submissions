class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapA = defaultdict(int)
        mapB = defaultdict(int)
        if len(s) != len(t):
             return False
        for num in range(len(s)):
            mapA[s[num]] += 1
            mapB[t[num]] += 1

        return mapA == mapB
        