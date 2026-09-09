class Solution:
    def hammingWeight(self, n: int) -> int:
        # and, or, not, xor, shift dx, shift sx
        res = 0
        while n != 0:
            # res += n % 2
            # n = n // 2

            # 1101 & 0001 = 0001 -> sommo 1 in quanto dispari
            # 1000 & 0001 = 0000 -> sommo 0 no resto in quanto pari
            res = res + (n & 1)   
            n = n >> 1  # divido per 2 (shift a destra)

        return res