class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0 
        start, end = 0, len(heights) - 1
        for i in range(len(heights)):
            while start < end: 
                volume = min(heights[start], heights[end]) * (end - start)
                maxArea = max(maxArea, volume)
                if heights[start] < heights[end]:
                    start += 1
                elif heights[start] > heights[end]:
                    end -= 1
                else: 
                    start += 1
                    end -= 1
        return maxArea 