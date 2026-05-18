class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for elem in strs: 
            result +=  str(len(elem)) + "#" + elem
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        idx = 0
        
        while idx < len(s):
            j = idx
            while s[j] != "#": 
                j+=1
            num = int(s[idx:j])
            result.append(s[j + 1: j + 1 + num])
            idx = j + 1 + num
        return result

            