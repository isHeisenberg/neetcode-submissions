class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # per esercizi di intervals in cui bisogna restituire una lista
        # MEGLIO crearne una nuova DA ZERO!
        # altrimenti incasinato con gli indici, insert, etc...
        stack = []
        intervals.sort()

        for interval in intervals:
            stack.append(interval)

            if len(stack) >= 2 and stack[-1][0] <= stack[-2][1]:
                temp = [
                    min(stack[-1][0], stack[-2][0]),
                    max(stack[-1][1], stack[-2][1])
                ]
                stack.pop()
                stack.pop()
                stack.append(temp)
        
        return stack
        