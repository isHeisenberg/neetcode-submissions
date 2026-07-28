class Solution:
    def maxArea(self, heights: List[int]) -> int:
        height = 0
        width = 0
        max_area = 0

        l = 0
        r = len(heights) - 1

        while l <= r:
            heigth = min(heights[l], heights[r])
            width = r - l
            max_area = max(max_area, heigth*width)

            if heights[l] <= heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1

        return max_area