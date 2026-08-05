class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        d = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        def dfs(i, c):
            if len(c) == len(digits):
                res.append(c)
                return
            for char in d[digits[i]]:
                c += char
                dfs(i + 1, c)
                c = c[:-1]                
        if digits: 
            dfs(0, "")
        return res