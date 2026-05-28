class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
            l, r = 0, 0 
            seen1, seen2 = defaultdict(int), defaultdict(int)
            
            if len(s2) < len(s1):
                return False 

            for i in range(len(s1)): 
                seen1[s1[i]] += 1
                seen2[s2[i]] += 1
                r += 1
                
            r -= 1

            while r <= len(s2) - 1 and l <= len(s2) - 1:
                if seen1 == seen2:
                    return True
                else:
                    if (seen2[s2[l]] - 1 == 0):
                        del(seen2[s2[l]])
                    else:
                        seen2[s2[l]] -= 1
                    l += 1
                    if r + 1 != len(s2):
                        r += 1
                        seen2[s2[r]] += 1
                    else: 
                        break

            return seen1 == seen2 
    