class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        # conteggio lettere di t
        count = {}
        for char in t:
            count[char] = 1 + count.get(char, 0)

        l = 0
        min_len = float("inf")
        stringa = ""

        for r in range(len(s)):
            letter = s[r]

            if letter in count:
                count[letter] -= 1

            # controlla se la finestra è valida
            while all(v <= 0 for v in count.values()):
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    stringa = s[l:r+1]

                if s[l] in count:
                    count[s[l]] += 1
                l += 1

        return stringa