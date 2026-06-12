"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        row = len(grid)
        col = len(grid[0])

        def util(i, j, r, c):
            
            if i == r and j == c:
                return Node(val=grid[i][j], isLeaf = True)
            
            halfR = (i + r) // 2
            halfC = (j + c) // 2
            leftUp = util(i, j, halfR, halfC)
            leftDown = util(halfR + 1, j, r, halfC)
            rightUp = util(i, halfC + 1, halfR, c)
            rightDown = util(halfR + 1, halfC + 1, r, c)
            
            if leftUp.isLeaf and rightUp.isLeaf and leftDown.isLeaf and rightDown.isLeaf and leftUp.val == leftDown.val == rightUp.val == rightDown.val:
                return Node(val = leftUp.val, isLeaf = True)
            else:
                node =  Node(val = 1, isLeaf = False)
                node.topLeft = leftUp
                node.topRight = rightUp
                node.bottomLeft = leftDown
                node.bottomRight = rightDown
                return node

        return util(0, 0, row - 1, col - 1)
            

            

                    
