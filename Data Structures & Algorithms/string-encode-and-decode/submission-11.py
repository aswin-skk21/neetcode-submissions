class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))
            res += '#'
            res += s
        return res
        

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        j = 0
        while i != len(s):
            j = i
            while s[i] != '#':
                i += 1
            num = int(s[j:i])
            word = s[i + 1: i + 1 + num]
            res.append(word)
            i = i + 1 + num
        return res