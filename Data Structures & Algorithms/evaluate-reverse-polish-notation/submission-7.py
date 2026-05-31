class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ['+', '-', '/', '*']

        for t in tokens:
            if len(stack) >= 2 and t in operations: 
                n1 = stack.pop()
                n2 = stack.pop()
                if t == '+':
                    stack.append(n2 + n1)
                elif t == '-':
                    stack.append(n2 - n1)
                elif t == '/':
                    stack.append(int(float(n2) / n1))
                else: 
                    stack.append(n2 * n1)
            else:
                stack.append(int(t))
        return stack[0]
