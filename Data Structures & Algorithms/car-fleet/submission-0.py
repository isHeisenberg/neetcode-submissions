class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # coppie posizione-velocità
        pairs = [(p, (target - p)/s) for p, s in zip(position, speed)]
        # ordino decrescente
        pairs.sort(reverse=True)
        
        stack = []
        
        # parto dalla fine quindi
        for _, time in pairs:
            stack.append(time)
            
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)