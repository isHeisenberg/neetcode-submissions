'''
KEY TAKEWAYS:

- isdigit(): per vedere se un char è una cifra

- num = num * 10 + int(char) per calcolarmi un numero
  cumulativo mentre sto iterando cifra per cifra
'''

# CON UN SOLO STACK ETEROGENEO
# ci metto tutto dentro anche i risultati nel mezzo
# infatti intere stringhe lunghe le calcolo e le metto
# se non è ] metto sempre dentro lo stack
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * substr)

        return "".join(stack)






# SOLUZIONE CON DUE STACK
'''
class Solution:
    def decodeString(self, s: str) -> str:
        stack_numbers = []
        stack_strings = []

        curr_string = ""
        num = 0

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)

            elif char == '[':
                stack_numbers.append(num)
                stack_strings.append(curr_string)

                num = 0
                curr_string = ""

            elif char == ']':
                k = stack_numbers.pop()
                prev_string = stack_strings.pop()

                curr_string = prev_string + curr_string * k

            else:
                curr_string += char

        return curr_string
'''







