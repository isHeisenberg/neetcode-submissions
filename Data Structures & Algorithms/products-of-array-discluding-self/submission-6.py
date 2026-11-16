class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        dx = [1] * len(nums)
        sx = [1] * len(nums)

        for i in range(1, len(nums)):
            sx[i] = nums[i-1] * sx[i-1]
         
        for i in range(len(nums)-2, -1, -1):
            dx[i] = nums[i+1] * dx[i+1] 

        res = []
        for i in range(len(nums)):
            res.append(sx[i] * dx[i])

        return res