class Solution:
    def maxArea(self, heights: List[int]) -> int:
        massimo = 0
        l, r = 0, len(heights) - 1

        while l < r:
            altezza = min(heights[l], heights[r])
            area = altezza * (r - l)
            massimo = max(massimo, area)

            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1
        
        return massimo