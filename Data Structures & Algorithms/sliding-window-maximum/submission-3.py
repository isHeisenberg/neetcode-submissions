class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []                # ci metto max per ogni window
        q = collections.deque() # qua invece gli indici (monotonic decreasing queue)
        l, r = 0, 0             # per la sliding window 


        while r < len(nums):   # non <= !!
            # ricorda sempre il check che q non sia vuota
            # inoltre smart mettere condizione direttamente lì
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
        
            # se left è out-of-bound rispetto alla window
            if l > q[0]:
                q.popleft()
            
            # devo mettere valore SSE ho almeno k elementi nella window all'inizio
            # se è grande come window, allora prossimo step supera
            # per cui solo qua posso aumentare l
            if (r+1) >= k:
                res.append(nums[q[0]])
                l += 1

            r += 1

        return res