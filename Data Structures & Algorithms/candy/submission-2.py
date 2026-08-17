class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        res = [1 for i in range(n)]
        for i in range(len(ratings) - 1):
            if ratings[i] < ratings[i+1]:
                res[i+1] = max(res[i+1], res[i] + 1)
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i+1]:
                res[i] = max(res[i], res[i+1] + 1)
        print(res)
        return sum(res)


