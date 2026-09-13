class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        N = len(points)
        for i in range(N):
            xi, yi = points[i]
            for j in range(i+1, N):
                xj, yj = points[j]
                d = abs(xi-xj) + abs(yi-yj)
                adj[i].append([d, j])
                adj[j].append([d, i])

        minheap = [(0, 0)]
        visit = set()
        res = 0

        while len(visit) < N:
            cost, node = heapq.heappop(minheap)
            if node in visit:
                continue

            visit.add(node)
            res += cost
            for neiCost, nei in adj[node]:
                if nei not in visit:
                    heapq.heappush(minheap, (neiCost, nei))    # qui pusho neiCost e basta, 

        return res


