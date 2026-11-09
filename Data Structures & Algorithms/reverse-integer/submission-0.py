class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)

        res = 0
        for n in range(len(str(x))-1, -1, -1):
            resto = x % 10
            x = x // 10
            res += resto * 10**n

        res *= sign

        if not -2**31 <= res <= 2**31 - 1:
            return 0

        return res