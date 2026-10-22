class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        pila = []
        res = [0] * len(temperatures) 

        for i, temp in enumerate(temperatures):
            while pila and temperatures[pila[-1]] < temp:
                idx = pila.pop()
                res[idx] = i - idx
            
            pila.append(i)

        return res