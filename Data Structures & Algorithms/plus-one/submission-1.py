class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        riporto = 1

        for i in range(len(digits) - 1, -1, -1):
            res = digits[i] + riporto

            digits[i] = res % 10
            riporto = res // 10

            if riporto == 0:
                return digits

        #digits.insert(0, 1)    # costa comunque O(n) pk shifto tutti gli elementi
        return [1] + digits     # più pulito

# NOTA BENE:
# O(n) tempo, chiaro
# O(n) spazio! Infatti ultima operazione creo una nuova lista lunga n+1