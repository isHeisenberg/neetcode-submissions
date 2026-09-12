class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxlen = 1
        stringa = s[0]

        # centro preciso
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                lunghezza = r - l + 1
                if lunghezza > maxlen:
                    maxlen = lunghezza
                    stringa = s[l:r+1]  # l:r+1, non solo r, pk limite sup escluso!

                l-=1
                r+=1

        # centro da due
        for i in range(len(s)):
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                lunghezza = r - l + 1
                if lunghezza > maxlen:
                    maxlen = lunghezza
                    stringa = s[l:r+1]

                l-=1
                r+=1


        return stringa



