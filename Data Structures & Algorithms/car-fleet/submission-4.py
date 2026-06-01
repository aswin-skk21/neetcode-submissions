class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
         p, s = zip(*sorted(zip(position, speed), reverse = True))
         stack = []

         for i in range(len(speed)):
            metric = (target - p[i]) / s[i] 
            if not stack or metric > stack[-1]:
                stack.append(metric)  
         return len(stack)