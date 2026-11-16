class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deads = set(deadends)

        if "0000" in deads:
            return -1

        queue = deque([("0000", 0)])
        visited = set()

        while queue:
            lock, times = queue.popleft()
            if lock == target:
                return times
            for i in range(4):
                for delta in [+1, -1]:
                    val = (int(lock[i]) + delta) % 10
                    newlock = lock[:i] + str(val) + lock[i+1:]
                    if newlock not in visited and newlock not in deads:
                        queue.append((newlock, times+1))
                        visited.add(newlock)
        return -1
