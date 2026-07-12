# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = collections.deque()
        stack.append(root)

        while(stack):
            size = len(stack)
            level = []

            for i in range(size):
                node = stack.popleft()
                if node:
                    level.append(node.val)
                    stack.append(node.left)
                    stack.append(node.right)
            if level: 
                res.append(level[-1])
        
        return res