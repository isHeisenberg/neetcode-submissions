class Solution:
    def isValid(self, s: str) -> bool:
        # metto in stack ([{
        parenthesis = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []

        for par in s:
            if par in parenthesis.values():
                stack.append(par)
            else:
                if stack and stack[-1] == parenthesis[par]:
                    stack.pop()
                else:
                    return False
        
        return not stack