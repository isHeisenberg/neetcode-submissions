class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        parenthesis = {')': '(', ']': '[', '}': '{'}

        for par in s:
            if par in parenthesis.values():
                stack.append(par)
            else:
                if stack and stack[-1] == parenthesis[par]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0