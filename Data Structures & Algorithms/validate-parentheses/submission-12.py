class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        check = {'}' : '{', ']' : '[', ')' : '('}

        for i in s: 
            if i in check.values():
                stack.append(i)
            else:
                if stack and check[i] == stack[-1]:
                    stack.pop()
                else:
                    return False 

        return True if not stack else False