class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentesi = {')': '(', ']': '[', '}': '{'}  # chiusa -> aperta

        for char in s:
            if char not in parentesi:               # è una parentesi APERTA
                stack.append(char)
            else:                                   # è una parentesi CHIUSA
                if not stack:                       # stack vuota, niente da matchare
                    return False
                if stack[-1] != parentesi[char]:    # la cima non corrisponde
                    return False
                stack.pop()                         # tutto ok, tolgo la cima

        return not stack # se rimane roba in stack, mancano chiusure