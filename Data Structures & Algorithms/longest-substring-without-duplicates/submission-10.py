class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = {}
        max_len = 0

        for r, ch in enumerate(s):
            # Controlli se ch è già dentro la finestra attuale: 
            # deve essere in seen e la sua ultima posizione deve essere >= l. 
            # Se la posizione è minore di l, 
            # quel carattere è fuori dalla finestra, quindi non è un duplicato.
            if ch in seen and seen[ch] >= l:
                l = seen[ch] + 1
            seen[ch] = r
            max_len = max(max_len, r - l + 1)

        return max_len