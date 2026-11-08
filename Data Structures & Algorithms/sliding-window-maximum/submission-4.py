# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         res = []
#         stack = []
#         l = 0

#         for r in range(len(nums)):

#             while stack and nums[stack[-1]] < nums[r]:
#                 stack.pop()

#             stack.append(r)

#             if stack[0] < l:
#                 stack.pop(0)  # COSTA O(n), NON VA BENE
                                # PER TOGLIERE DA DAVANTI MEGLIO DEQUE

#             if (r - l) == k - 1:
#                 res.append(nums[stack[0]])
#                 l += 1

#         return res


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        dq = deque()
        l = 0

        for r in range(len(nums)):

            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()
            dq.append(r)

            # mi raccomando, altrimenti se il massimo è all'inizio
            # rischio di portarmelo dietro all'infinito
            # per cui check su primo elemento per eliminarlo
            if dq[0] < l:
                dq.popleft()    # NECESSARIA DEQUE, altrimenti costa O(n) con lista

            if r - l == k - 1:
                res.append(nums[dq[0]])
                l += 1

        return res
