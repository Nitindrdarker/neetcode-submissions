# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def util(root):
            if root == None:
                return [0, 0]

            tookLeft, leftLeft = util(root.left)
            tookRight, leftRight = util(root.right)
            took = leftLeft + leftRight + root.val
            skip = max(tookLeft, leftLeft) + max(tookRight, leftRight)
            
            return [took, skip]
        
        return max(util(root))