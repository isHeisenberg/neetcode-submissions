'''
ui -> vi con ti
{ui: [(vi,ti), ...]}
visited = set()
heap = []
'''
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v,t))
        
        visited = set()
        heap = [(0, k)]
        result = -1

        while heap:
            time, node = heapq.heappop(heap)
            if node in visited:
                continue
            result = max(result, time)
            visited.add(node)
            if len(visited) == n:
                return result
            
            for v,t in adj[node]:
                if v not in visited:
                    heapq.heappush(heap, (time+t, v))

        return -1






