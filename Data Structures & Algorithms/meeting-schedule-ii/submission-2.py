"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

# con min-heap in cui metto gli end
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        heap = []

        for interval in intervals:
            start, end = interval.start, interval.end

            # Se una sala è libera, riutilizzala
            if heap and heap[0] <= start:
                heapq.heappop(heap)

            # Inserisci la fine del meeting
            heapq.heappush(heap, end)

        return len(heap)
