class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        l1 = len(word1)
        l2 = len(word2)
        memo = [[[l1+l2] for i in range(l2+1)] for j in range(l1+1)]
        for i in range(l1, -1, -1):
            for j in range(l2, -1, -1):
                if j >= l2 and i >= l1:
                    memo[i][j] = 0
                    continue
                if j >= l2:
                    memo[i][j] = l1 - i
                    continue
                if i >= l1:
                    memo[i][j] = l2 - j
                    continue
                if word1[i] == word2[j]:
                    skipped = memo[i+1][j+1]
                    memo[i][j] = skipped
                else:
                    deleted = memo[i+1][j] + 1
                    inserted = memo[i][j+1] + 1
                    replaced = memo[i+1][j+1] + 1
                    memo[i][j] = min(deleted, inserted, replaced)
        return memo[0][0]

                    




        # memo = {}

        # def util(i, j):
        #     if j >= l2 and i >= l1:
        #         return 0
        #     if j >= l2:
        #         return l1 - i
        #     if i >= l1:
        #         return l2 - j
        #     if (i, j) in memo:
        #         return memo[(i, j)]

        #     skipped = deleted = inserted = replaced = l1 + l2
        #     if word1[i] == word2[j]:
        #         skipped = util(i+1, j+1)
        #         memo[(i, j)] = skipped
        #         return skipped
        #     else:
        #         deleted = util(i+1, j) + 1
        #         inserted = util(i, j+1) + 1
        #         replaced = util(i+1, j+1) + 1
        #         memo[(i, j)] = min(deleted, inserted, replaced)
        #         return memo[(i, j)]
        # return util(0, 0)
