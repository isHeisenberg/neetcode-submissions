class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            if not stack or temperatures[stack[-1]] >= temperatures[i]:
                stack.append(i)
            else:
                # RICORDA SEMPRE IL CHECK SU STACK OVUNQUE!
                while stack and temperatures[stack[-1]] < temperatures[i]:
                    idx = stack.pop()
                    res[idx] = i - idx
                stack.append(i) # dopo aver levato, metto i

        return res
