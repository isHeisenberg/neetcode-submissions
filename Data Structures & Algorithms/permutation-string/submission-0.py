class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count = {}

        # Conta lettere di s1
        for c in s1:
            count[c] = 1 + count.get(c, 0)

        l = 0

        for r in range(len(s2)):
            # aggiungi carattere alla finestra
            c = s2[r]
            if c in count:
                count[c] -= 1

            # mantieni finestra della stessa lunghezza
            if r - l + 1 > len(s1):
                left_char = s2[l]
                if left_char in count:
                    count[left_char] += 1
                l += 1

            # controlla se tutti i valori sono zero
            if all(v == 0 for v in count.values()):
                return True

        return False


        