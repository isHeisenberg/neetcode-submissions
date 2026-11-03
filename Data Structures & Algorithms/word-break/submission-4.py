
from functools import cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        @cache
        def dfs(parola):
            if parola == "":
                return True
            
            for word in wordDict:
                lunghezza = len(word)
                # 
                # if lunghezza <= len(s) and parola[:lunghezza] == word:
                #     dfs(parola[lunghezza:])
                if parola[:lunghezza] == word:
                    if dfs(parola[lunghezza:]):
                        return True

            return False    # devi ricordati fuori in caso False
        
        return dfs(s)