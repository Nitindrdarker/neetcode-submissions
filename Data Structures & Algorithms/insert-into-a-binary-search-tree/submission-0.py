# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def util(root):
            if root == None:
                return TreeNode(val = val)
            if root.val > val:
                root.left = util(root.left)
            elif root.val < val:
                root.right = util(root.right)
            return root
        return util(root)
                