"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # intervals.sort() non va bene, pk è una classe nuova Interval!
        intervals.sort(key=lambda x: x.start)
        heap = []
        maxlen = 0

        for interval in intervals:
            start, end = interval.start, interval.end
            while heap and heap[0] <= start:
                heapq.heappop(heap)
            heapq.heappush(heap, end)

            maxlen = max(maxlen, len(heap))

        return maxlen