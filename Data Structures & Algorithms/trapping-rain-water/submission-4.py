class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lMax, rMax = height[l], height[r]
         
        res = 0  
        while l < r: 
            if lMax < rMax: 
                l += 1
                lMax = max(lMax, height[l])
                if lMax - height[l] > 0: 
                    res += lMax - height[l]
            else:
                r -= 1
                rMax = max(rMax, height[r])
                if rMax - height[r] > 0: 
                    res += rMax - height[r]
        return res