"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution: 
    def canAttendMeetings(self, intervals: List[Interval]) -> bool: 
        intervals.sort(key=lambda x: x.start, reverse=False)

        # più elegante partendo da 1 e usando i e i-1
        # infatti se fosse vuoto -> range(1, 0) NON ENTRA MAI NEL CICLO
        for i in range(1,len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                return False

        return True