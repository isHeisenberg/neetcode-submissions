class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for i in range(1, len(strs)):
            j = 0
            # check tutte le lettere fino a quando una delle due termina
            while j < min(len(prefix), len(strs[i])):
                if prefix[j] != strs[i][j]:
                    break
                j += 1
            
            prefix = prefix[:j] # mi prendo solo i caratteri in cui erano uguali
        
        return prefix