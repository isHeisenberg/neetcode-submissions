class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # più piccolo degli altri e non overlappa più
            # quello nuovo è saltato totalmente (inizio interval > fine nuovo)
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:] # appendo il resto dell'array (easy usando il +)
            # più grande, appendo da lista
            # se quello nuovo salta l'altro totalmente (inizio nuovo > fine interval)
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                # merge degli intervalli -> comodo usando MIN e MAX
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]
        res.append(newInterval) # ricorda di appendere newInterval
        return res