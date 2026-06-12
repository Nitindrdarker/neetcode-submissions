# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def util(root, currMax):
            if root == None:
                return 
            if root.val >= currMax:
                self.count += 1
            util(root.left, max(root.val, currMax))
            util(root.right, max(root.val, currMax))
            return 
        util(root, root.val)
        return self.count