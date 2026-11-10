class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = 0
        multiplier = 1

        for i in range(len(num2) - 1, -1, -1):
            digit2 = int(num2[i])

            curr = 0
            power = 1

            for j in range(len(num1) - 1, -1, -1):
                digit1 = int(num1[j])

                curr += digit1 * digit2 * power
                power *= 10

            res += curr * multiplier
            multiplier *= 10

        return str(res)