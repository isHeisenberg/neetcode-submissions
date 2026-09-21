class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = [0]
        somma = 0
        for op in operations:
            if op == 'C':
                somma -= stack.pop()
            elif op == 'D':
                stack.append(stack[-1] * 2)
                somma += stack[-1]
            elif op == '+':
                stack.append(stack[-1] + stack[-2])
                somma += stack[-1]
            else:
                stack.append(int(op))
                somma += stack[-1]

        return somma