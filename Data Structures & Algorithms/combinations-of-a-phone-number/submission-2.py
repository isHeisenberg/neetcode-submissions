'''
Subsets: per ogni elemento hai due possibilità (includerlo o escluderlo).
Letter Combinations: per ogni posizione hai N possibilità, una per ogni lettera associata alla cifra.
'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = []
        sol = []

        phone = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
        }

        def dfs(i):
            if i == len(digits):
                res.append("".join(sol))
                return

            for letter in phone[digits[i]]:
                sol.append(letter)
                dfs(i+1)
                sol.pop()
                # non serve il secondo dfs(i+1)
                # non è come subsets in cui le scelte si hanno togliendo
                # qua esploro tutte le opzioni grazie al for    

        dfs(0)
        return res



