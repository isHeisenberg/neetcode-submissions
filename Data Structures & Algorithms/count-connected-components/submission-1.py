class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # {1: 0,2  0: 1 2: 1 3: 4 4: 3}
        edgs = defaultdict(list)
        for edge in edges:
            edgs[edge[0]].append(edge[1])
            edgs[edge[1]].append(edge[0])

        visited = set()
        counter = 0

        def bfs(i):
            queue = deque([i])
            visited.add(i)

            while queue:
                node = queue.popleft()
                for e in edgs[node]:
                    if e not in visited:
                        queue.append(e)
                        visited.add(e)

        for i in range(n):
            if i not in visited:
                bfs(i)
                counter += 1

        return counter