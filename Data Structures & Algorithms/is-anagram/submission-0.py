class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dictS, dictT = {}, {}

        for num in range(len(s)):
            dictS[s[num]] = dictS.get(s[num], 0) + 1
            dictT[t[num]] = dictT.get(t[num], 0) + 1


        return dictS == dictT