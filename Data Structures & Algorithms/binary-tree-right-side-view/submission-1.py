# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = collections.deque()
        q.append(root)
        res = []
        while q:
            l = len(q)
            lastVal = 0
            for _ in range(l):
                node = q.popleft()
                lastVal = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(lastVal)
        return res
                