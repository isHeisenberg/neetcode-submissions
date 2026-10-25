class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        stack = []
        removed = 0

        # greedy approach
        # se nuovo elemento ha estremo maggiore e overlappa non lo considero, altrimento switcho
        for interval in intervals:
            if stack and stack[-1][1] > interval[0]:
                if stack[-1][1] > interval[1]:
                    stack[-1] = interval
                removed += 1
            else:
                stack.append(interval)

        return removed
