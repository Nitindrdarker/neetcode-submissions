# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def util(root, val):
            if root == None:
                return None
            if root.val == val:
                
                if root.left == None and root.right == None:
                    return None
                elif root.left == None:
                    return root.right
                elif root.right == None:
                    return root.left
                else:
                    node = root.right
                    while node.left:
                        node = node.left
                    root.val = node.val
                    print(root.right.val, node.val)
                    root.right = util(root.right, node.val)
                    return root
            root.left = util(root.left, val)
            root.right = util(root.right, val)
            return root
        return util(root, val)




                