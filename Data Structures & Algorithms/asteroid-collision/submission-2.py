class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            # while stack:
            #     if stack[-1] > 0 and ast < 0:     # versi per scontrarsi
            # così, altrimenti se trova due -> -> non entra in if e continua all'inf!
            # comodo mettere condizione aggiuntiva diretta nel while
            while stack and stack[-1] > 0 and ast < 0:              
                # tre casi
                if abs(stack[-1]) < abs(ast):
                    stack.pop()
                elif abs(stack[-1]) == abs(ast):
                    stack.pop()
                    ast = 0
                    break
                else:
                    ast = 0
                    break

            if ast != 0:
                stack.append(ast)

        return stack
            
                     