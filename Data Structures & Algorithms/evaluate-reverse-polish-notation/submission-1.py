class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = {'+', '-', '*', '/'}
        
        for t in tokens:
            if t not in operands:
                stack.append(int(t))
            else:
                a = stack.pop()
                b = stack.pop()
                if t == '+':
                    stack.append(b+a)
                elif t == '-':
                    stack.append(b-a)
                elif t == "*":
                    stack.append(b*a)
                else:
                    stack.append(int(b/a)) # devo metterci SOLO integer
        
        return stack[-1]