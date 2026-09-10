class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = curSum = 0
        # questo prende casi in cui preciso = 0
        prefixSums = { 0 : 1 }

        for num in nums:
            curSum += num
            diff = curSum - k   # quanto mi manca per fare k lo cercherò nel dict

            # sommo per tutte le volte in cui prima c'è quel valore
            res += prefixSums.get(diff, 0)
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)

        return res