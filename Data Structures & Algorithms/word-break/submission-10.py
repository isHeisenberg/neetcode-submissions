class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def dfs(string):
            if string == "":
                return True
            if string in memo:
                return memo[string]

            for word in wordDict:
                if string.startswith(word):
                    if dfs(string[len(word):]):
                        memo[string] = True
                        return True
            memo[string] = False
            return False

        return dfs(s)
