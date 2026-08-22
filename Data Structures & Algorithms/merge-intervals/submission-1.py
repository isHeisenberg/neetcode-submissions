class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []

        curr = intervals[0]
        for i in range(1, len(intervals)):
            if curr[1] >= intervals[i][0]:
                curr = [curr[0], max(curr[1], intervals[i][1])]
            else:
                res.append(curr)
                curr = intervals[i]

        res.append(curr)
        return res  