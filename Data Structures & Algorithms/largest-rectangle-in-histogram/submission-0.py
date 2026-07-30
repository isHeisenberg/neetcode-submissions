class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []  # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h: # se trovo colonna più bassa fermo e pop
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index)) # calcolo indietro fino a index
                start = index # come se nuova colonna esistesse da dietro fino a index

            stack.append((start, h))

        for i, h in stack: # aree per quelli rimasti nello stack
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea