class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapA = {}
        mapB = {}
        if len(s) != len(t):
             return False
        for num in range(len(s)):
            mapA[s[num]] = mapA.get(s[num], 0) + 1
            mapB[t[num]] = mapB.get(t[num], 0) + 1

        return mapA == mapB
        