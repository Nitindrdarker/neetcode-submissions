class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        count = {}
        heapq.heapify(meetings)
        meetingQ = []
        emptyRoom = [i for i in range(n)]
        heapq.heapify(emptyRoom)
        mx = 0
        t = 0
        while meetings:
            s, e = meetings[0]
            if emptyRoom:
                heapq.heappop(meetings)
                t = max(s, t)
                while meetingQ and meetingQ[0][0] <= t:
                    endTime,room = heapq.heappop(meetingQ)
                    heapq.heappush(emptyRoom, room)
                room = heapq.heappop(emptyRoom)
                heapq.heappush(meetingQ, ((e - s) + t, room))
                count[room] = count.get(room, 0) + 1
                mx = max(count[room], mx)
            else:
                t = max(t, meetingQ[0][0])
                while meetingQ and meetingQ[0][0] <= t:
                    endTime,room = heapq.heappop(meetingQ)
                    heapq.heappush(emptyRoom, room)
                    
        for i in range(n):
            if count[i] == mx:
                return i
