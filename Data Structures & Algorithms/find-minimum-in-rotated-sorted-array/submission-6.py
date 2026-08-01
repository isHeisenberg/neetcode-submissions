class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        # non <=, così mi fermo quando l == r, cioè convergo a punto unico
        while l < r:
            mid = (l+r) // 2

            if(nums[mid] > nums[r]): # qui scarto mid perchè sicuro non è il minimo
                l = mid + 1
            else : # (nums[mid] < nums[l]): qui non lo scarto perchè 
                    # potrebbe essere il minimo, infatti mid < l !!!
                r = mid

        # a questo punto l == r, non conviene usare mid, potrebbe non convergere a punto
        return nums[l]