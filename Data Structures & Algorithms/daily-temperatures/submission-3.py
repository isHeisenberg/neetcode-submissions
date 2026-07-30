class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        length = len(temperatures)
        res = [0] * length
        
        for t, temp in enumerate(temperatures):
            # uso temp invece di temperatures[t]
            while stack and temp > temperatures[stack[-1]]:
                res[stack[-1]] = t - stack[-1]
                stack.pop()

            stack.append(t)
        
        return res