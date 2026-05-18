class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        DictS, DictT = {}, {}

        for num in range(len(s)):
            DictS[s[num]] = DictS.get(s[num], 0) + 1
            DictT[t[num]] = DictT.get(t[num], 0) + 1

        return DictS == DictT
            

