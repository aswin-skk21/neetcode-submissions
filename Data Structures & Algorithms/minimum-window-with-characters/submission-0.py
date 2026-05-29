class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res, resLen = [-1, -1], float('inf')
        if len(t) > len(s) or t == "": 
            return ""
        
        T, S = defaultdict(int), defaultdict(int)

        for i in range(len(t)):
            T[t[i]] += 1

        have, need = 0, len(T)
        
        l = 0
        for r in range(len(s)):
            S[s[r]] += 1
            if s[r] in T and T[s[r]] == S[s[r]]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = [l, r]
                S[s[l]] -= 1
                if s[l] in T and S[s[l]] < T[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r + 1] if resLen != float('inf') else ""