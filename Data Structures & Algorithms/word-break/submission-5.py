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
from functools import cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        @cache
        def dfs(parola):
            if parola == "":
                return True
            
            for word in wordDict:
                lunghezza = len(word)

                # if lunghezza <= len(s) and parola[:lunghezza] == word:
                #     dfs(parola[lunghezza:])
                if parola[:lunghezza] == word:
                    if dfs(parola[lunghezza:]):
                        return True

            return False    # devi ricordati fuori in caso False
        
        return dfs(s)
'''

