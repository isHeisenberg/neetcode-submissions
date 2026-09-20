class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n       # riga finale sono tutti '1'

        for i in range(m-1):
            # messi tutti a '1', verranno aggiornati tutti tranne ultimo in colonna ('1')
            newRow = [1] * n    
            for j in range(n-2, -1, -1):    # ciclo ma non prendo ultimo così non implode
                newRow[j] = newRow[j+1] + row[j]
            row = newRow
        
        return row[0]

    