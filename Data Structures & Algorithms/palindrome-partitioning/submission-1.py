class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        def dfs(j, i):
            if i >= len(s):
                if i == j:
                    res.append(part.copy())
                return

            if self.isPali(s, j, i):
                part.append(s[j : i + 1])
                dfs(i + 1, i + 1)
                part.pop()

            dfs(j, i + 1)

        dfs(0, 0)
        return res

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True


'''
Time complexity: 
O(n * 2^n)

Space complexity:
O(n) extra space.
O(n * 2^n) space for the output list.
'''






'''
Leggera ottimizzazione
Mi pre-calcolo tutti i possibili palindromi (DP)
così poi check è O(1)

n = len(s)
dp = [[False] * n for _ in range(n)]
for r in range(n):
    for l in range(r + 1):
        if s[l] == s[r] and (r - l <= 2 or dp[l + 1][r - 1]):
            dp[l][r] = True
'''
