class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            # MODO PER OTTENERE LE CIFRE DI UN NUMERO
            # 123 % 10 = 3
            # 123 // 10 = 12
            # 12 % 10 = 2
            # 12 // 10 = 1
            # 1 % 10 = 1
            # 1 // 10 = 0
            somma = 0
            while n != 0:
                resto = n % 10
                n = n // 10
                somma += resto**2
            
            n = somma
            if n in seen:
                return False

            seen.add(n)

        return True
