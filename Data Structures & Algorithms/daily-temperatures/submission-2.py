class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        length = len(temperatures)
        res = [0] * length
        for t in range(length):
            # while temperatures[t] > temperatures[stack[-1]]:
            while stack and temperatures[t] > temperatures[stack[-1]]:
                res[stack[-1]] = t - stack[-1]
                stack.pop()

            stack.append(t)
        
        return res
            
