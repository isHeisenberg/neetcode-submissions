'''
CHECK VALID STRING: Two Stacks
DUE STACK: Due tipi di elementi da gestire separatamente

- parentesi: indici delle '(' non ancora chiuse
- stars: indici delle '*'

A fine scansione, ogni '(' rimasta può usare una '*' successiva come ')'
'''
class Solution:
    def checkValidString(self, s: str) -> bool:
        # utilizzo due stack
        parentesi = []
        stars = []

        for idx, char in enumerate(s):
            if char == '(':
                parentesi.append(idx)
            elif char == '*':
                stars.append(idx)
            else:
                if not parentesi:
                    if not stars:
                        return False
                    else:
                        stars.pop()
                else:
                    parentesi.pop()

        # potrebbero essere rimaste delle '('
        # se ho delle '*' le posso utilizzare
        if not parentesi:
            return True
        # caso ho (, ma non *
        if not stars:
            return False
        
        # provo a svuotare le parentesi
        while parentesi:
            if not stars or parentesi[-1] > stars[-1]:
                return False
            parentesi.pop()
            stars.pop()

        return True


















