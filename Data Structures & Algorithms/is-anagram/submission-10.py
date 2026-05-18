class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapA = {}
        mapB = {}
        if len(s) != len(t):
             return False
        for a, b in zip(s, t):
            mapA[a] = mapA.get(a, 0) + 1
            mapB[b] = mapB.get(b, 0) + 1

        return mapA == mapB
        