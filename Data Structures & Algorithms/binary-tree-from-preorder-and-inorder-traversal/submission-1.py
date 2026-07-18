# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        start = 0
        while inorder[start] != preorder[0]:
            start += 1
            
        root.left = self.buildTree(preorder[1:start + 1], inorder[:start])
        root.right = self.buildTree(preorder[start + 1:], inorder[start + 1:])

        return root