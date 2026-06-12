# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def util(root):
            if root == None:
                return 0
            left = util(root.left)
            right = util(root.right)
            if left == -1 or right == -1:
                return -1
            if abs(right - left) > 1:
                return -1
            return max(left, right) + 1
        v = util(root)
        if v == -1:
            return False
        return True
        
            
            
        