class Solution:
    def hammingWeight(self, n: int) -> int:
        # and, or, not, xor, shift dx, shift sx
        res = 0
        while n != 0:
            res += n % 2
            n = n // 2

        return res