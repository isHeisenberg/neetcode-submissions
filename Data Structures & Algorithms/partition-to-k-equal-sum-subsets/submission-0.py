class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False

        nums.sort(reverse=True)
        target = sum(nums) // k
        used = [False] * len(nums)

        def backtrack(i, k, subsetSum):
            if k == 0:
                return True
            if subsetSum == target:
                return backtrack(0, k - 1, 0)

            '''
            # Includo nums[i]
            used[i] = True
            if backtrack(i + 1, k, subsetSum + nums[i]):
                return True
            used[i] = False

            # Escludo nums[i]
            if backtrack(i + 1, k, subsetSum):
                return True
            '''
            
            # con il ciclo for mi posso gestire i casi inutili
            # altrimenti creo alberi inutili che gestisco in un base case
            for j in range(i, len(nums)):
                if used[j] or subsetSum + nums[j] > target:
                    continue
                used[j] = True
                # solo se true faccio return, altrimenti non va in used[j] dopo
                if backtrack(j + 1, k, subsetSum + nums[j]):
                    return True
                used[j] = False

            return False

        return backtrack(0, k, 0)