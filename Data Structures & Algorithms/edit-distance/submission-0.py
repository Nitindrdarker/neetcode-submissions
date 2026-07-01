class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        l1 = len(word1)
        l2 = len(word2)
        memo = {}

        def util(i, j):
            if j >= l2 and i >= l1:
                return 0
            if j >= l2:
                return l1 - i
            if i >= l1:
                return l2 - j
            if (i, j) in memo:
                return memo[(i, j)]

            skipped = deleted = inserted = replaced = l1 + l2
            if word1[i] == word2[j]:
                skipped = util(i+1, j+1)
                memo[(i, j)] = skipped
                return skipped
            else:
                deleted = util(i+1, j) + 1
                inserted = util(i, j+1) + 1
                replaced = util(i+1, j+1) + 1
                memo[(i, j)] = min(deleted, inserted, replaced)
                return memo[(i, j)]
        return util(0, 0)
