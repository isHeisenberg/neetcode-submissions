class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # per esercizi di intervals in cui bisogna restituire una lista
        # MEGLIO crearne una nuova DA ZERO!
        # altrimenti incasinato con gli indici, insert, etc...
        stack = []
        intervals.sort()

        # for interval in intervals:
        #     stack.append(interval)

        #     if len(stack) >= 2 and stack[-1][0] <= stack[-2][1]:
        #         temp = [
        #             min(stack[-1][0], stack[-2][0]),
        #             max(stack[-1][1], stack[-2][1])
        #         ]
        #         stack.pop()
        #         stack.pop()
        #         stack.append(temp)

        # più pulito, tanto min non serve pk è ordinato e no bisogno di pop, basta modifica
        for interval in intervals:
            if stack and interval[0] <= stack[-1][1]:
                stack[-1][1] = max(stack[-1][1], interval[1])
            else:
                stack.append(interval)
        
        return stack
        