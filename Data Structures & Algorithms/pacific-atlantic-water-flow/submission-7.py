class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        pac = set()
        atl = set()

        def bfs(starts, visit):
            q = collections.deque(starts)

            while q:
                r, c = q.popleft()
                if (r, c) in visit:
                    continue

                visit.add((r, c))

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if (nr in range(ROWS) and nc in range(COLS)
                        and (nr, nc) not in visit
                        and heights[nr][nc] >= heights[r][c]):
                        q.append((nr, nc))

        # qua ci metto tutte le celle dei bordi corrispettivi
        pac_starts = []
        atl_starts = []

        # Bordi superiore/inferiore
        for c in range(COLS):
            pac_starts.append((0, c))
            atl_starts.append((ROWS - 1, c))

        # Bordi sinistro/destro
        for r in range(ROWS):
            pac_starts.append((r, 0))
            atl_starts.append((r, COLS - 1))

        # faccio bfs partendo da tali celle
        bfs(pac_starts, pac)
        bfs(atl_starts, atl)

        res = []

        for r in range(ROWS):
            for c in range(COLS):
                # se visitato in entrambi allora va da un oceano all'altro
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res



