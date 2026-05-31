class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if len(stack) >= 2: 
                if t == '+':
                    a, b = stack.pop(), stack.pop()
                    stack.append(b + a)
                elif t == '-':
                    a, b = stack.pop(), stack.pop()
                    stack.append(b - a)
                elif t == '/':
                    a, b = stack.pop(), stack.pop()
                    stack.append(int(float(b) / a))
                elif t == '*':  
                    a, b = stack.pop(), stack.pop()
                    stack.append(b * a)
                else:
                    stack.append(int(t))
            else:
                stack.append(int(t))
        return stack[0]
