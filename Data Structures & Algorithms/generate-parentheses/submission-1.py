class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        stack = []
        res = []

        def backtrack(openN, closedN):
            # valid IIF open == closed == n
            if openN == closedN == n:
                res.append("".join(stack))
                return

            # only add open paranthesis if open < n
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()

            # only add a closing paranthesis if closed < open
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res