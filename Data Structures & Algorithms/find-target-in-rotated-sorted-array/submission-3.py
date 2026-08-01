class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        # cerco
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            # metà sinistra ordinata
            if nums[l] <= nums[mid]:
                # t = 1, se tipo 4,5,6,7,8,1,2,3, mid = 7: t<7, ma NON c'è a sx! 1<4!
                # dunque doppia condizione
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # metà destra ordinata
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1