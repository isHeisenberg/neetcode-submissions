class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def dfs(parola):
            if parola == "":
                return True  # Ho consumato tutta la stringa

            if parola in memo:
                return memo[parola]  # Ho già risolto questo sottoproblema

            for word in wordDict:
                if parola.startswith(word):  # La parola è un prefisso valido
                    if dfs(parola[len(word):]):  # Provo sulla parte rimanente
                        memo[parola] = True
                        return True  # Ho trovato una segmentazione valida

            memo[parola] = False  # Nessuna combinazione ha funzionato
            return False

        return dfs(s)



'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]
'''

