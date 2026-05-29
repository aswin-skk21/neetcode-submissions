class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        sA, sB = [0] * 26, [0] * 26

        for i in range(len(s1)):
            sA[ord(s1[i]) - ord("a")] += 1
            sB[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(len(sA)):
            if sA[i] == sB[i]:
                matches += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            idx = ord(s2[r]) - ord('a')
            sB[idx] += 1
            if sB[idx] == sA[idx]:
                matches += 1
            elif sA[idx] + 1 == sB[idx]:
                matches -= 1

            idx = ord(s2[l]) - ord('a')
            sB[idx] -= 1
            if sB[idx] == sA[idx]:
                matches += 1
            elif sA[idx] - 1 == sB[idx]:
                matches -= 1
            l += 1
        return matches == 26
