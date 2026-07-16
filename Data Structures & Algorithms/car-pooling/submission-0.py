class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        mx = 0
        for c, f, t, in trips:
            mx = max(mx, t)

        road = [0] * (mx+1)

        for c, f, t in trips:
            road[f] += c
            road[t] -= c
        # print(road)
        for i in range(1, len(road)):
            road[i] += road[i-1]
            # print(road)
            if road[i] > capacity:
                return False
        return True
            

        

