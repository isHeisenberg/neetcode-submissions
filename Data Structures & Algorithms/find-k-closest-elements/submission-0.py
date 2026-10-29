class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # lower-bound binary search
        l, r = 0, len(arr)

        while l < r:
            mid = (l + r) // 2

            if arr[mid] < x:
                l = mid + 1
            else:
                r = mid

        # primo elemento >= x
        l, r = l - 1, l

        # espando a sx e dx
        while r - l - 1 < k:
            if l < 0:
                r += 1
            elif r >= len(arr):
                l -= 1
            elif abs(arr[l] - x) <= abs(arr[r] - x):
                l -= 1
            else:
                r += 1

        return arr[l + 1:r]