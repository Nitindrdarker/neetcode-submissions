class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {}
        for frm, to in tickets:
            if frm not in adj:
                adj[frm] = []
            heapq.heappush(adj[frm], to)
        completed = []
        visited = set()
        done = set()
        def util(node):
            if node in visited:
                return 
            if node in done:
                return
            if node in adj:
                neighs = adj[node]
                while neighs:
                    neigh = heapq.heappop(neighs)
                    util(neigh)
            done.add(node)
            completed.append(node)
            

        util("JFK")
        return completed[::-1]
                



            
