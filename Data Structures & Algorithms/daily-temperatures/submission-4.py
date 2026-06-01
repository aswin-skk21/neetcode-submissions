class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                end = stack.pop()
                result[end] = i - end
            if len(stack) == 0 or temperatures[i] <= temperatures[stack[-1]]: 
                stack.append(i)
    
        
        return result
