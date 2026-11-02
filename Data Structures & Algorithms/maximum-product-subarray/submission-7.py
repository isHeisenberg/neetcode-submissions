class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]   # inizializzo res sempre con un valore che ho 
        minimo, massimo = 1, 1

        for num in nums:
            temp = massimo * num    # dato che viene modificato max in mezzo
            massimo = max(massimo * num, minimo * num, num)
            minimo = min(temp, minimo * num, num)   # uso qua temp
            res = max(res, massimo)
        
        return res

'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        massimo = nums[0]
        # dp[x][y] = prodotto dei numeri del subarray nums[x:y+1]
        dp = [ [1] * n for _ in range(n) ]
        for i in range(n):
            dp[i][i] = nums[i]
            # se non lo facessi, gli altri singoli elementi
            # non verrebbero mai checkati dato che length almeno 2!!!
            massimo = max(massimo, nums[i])
        
        for length in range(2, n+1):
            for i in range(n - length + 1):
                j = i + length - 1
                prodotto = nums[j] * dp[i][j-1]
                dp[i][j] = prodotto
                massimo = max(prodotto, massimo)
        
        return massimo
'''


