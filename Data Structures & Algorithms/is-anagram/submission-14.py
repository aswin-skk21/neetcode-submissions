class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        one = defaultdict(int)
        two = defaultdict(int)

        if len(s) != len(t):
            return False
            
        for i in range(len(s)): 
            one[s[i]] += 1
            two[t[i]] += 1
        
        return one == two
        