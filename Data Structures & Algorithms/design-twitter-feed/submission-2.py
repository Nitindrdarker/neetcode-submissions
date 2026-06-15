class Twitter:

    def __init__(self):
        self.timeStamp = 0
        self.postMap = defaultdict(list) #id - postID
        self.followerMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.postMap[userId].append((self.timeStamp, tweetId))
        self.timeStamp += 1

    def pushToHeap(self,minHeap, t, id):
        
        if len(minHeap) < 10:
            heapq.heappush(minHeap, (t, id))
        else:
            if t > minHeap[0][0]:
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, (t, id))
        return minHeap

    def getNewsFeed(self, userId: int) -> List[int]:
        # nLogN
        #selfposts
        l = []
        for t, id in self.postMap[userId]:
            self.pushToHeap(l ,t, id)
        for follower in self.followerMap[userId]:
            for t, id in self.postMap[follower]:
                self.pushToHeap(l, t, id)
        res = []
        while l:
            _, id = heapq.heappop(l)
            res.append(id)
        return res[::-1]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.followerMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followeeId in self.followerMap[followerId]:
            self.followerMap[followerId].remove(followeeId)

        
