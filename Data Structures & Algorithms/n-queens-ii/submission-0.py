class Solution:
    def totalNQueens(self, n: int) -> int:
        colVisited = set()
        posDiagVisited = set()
        negDiagVisited = set()
        row = col = n
        res = []
        def util(i):
            if i >= row:
                return 1
            v = 0
            for j in range(col):
                if j in colVisited:
                    continue
                posDiag = i - j
                negDiag = i + j
                if posDiag in posDiagVisited:
                    continue
                if negDiag in negDiagVisited:
                    continue
                colVisited.add(j)
                posDiagVisited.add(posDiag)
                negDiagVisited.add(negDiag)
                
                v += util(i+1)
                
                colVisited.remove(j)
                posDiagVisited.remove(posDiag)
                negDiagVisited.remove(negDiag)
            return v
        return util(0)
        