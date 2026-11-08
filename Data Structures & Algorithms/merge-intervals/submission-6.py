class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        stack = []

        for interval in intervals:
            if not stack or stack[-1][1] < interval[0]:
                stack.append(interval)
            else:
                stack[-1] = [stack[-1][0], max(stack[-1][1], interval[1])]
        
        return stack
