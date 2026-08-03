class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        subset = ""

        def backtrack(o, c):
            nonlocal subset
            if len(subset) == (n * 2):
                res.append(subset)
                return
            if o < n:
                subset += "("
                backtrack(o + 1, c)
                subset = subset[:-1]
            if c < o:
                subset += ")"
                backtrack(o, c + 1)
                subset = subset[:-1]
        
        backtrack(0, 0)
        return res