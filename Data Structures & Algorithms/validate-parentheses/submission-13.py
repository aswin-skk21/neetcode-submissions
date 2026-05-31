class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        check = {'}' : '{', ']' : '[', ')' : '('}

        for i in s: 
            if i in check:
                if stack and check[i] == stack[-1]:
                    stack.pop()
                else:
                    return False 
            else: 
                stack.append(i)

        return True if not stack else False