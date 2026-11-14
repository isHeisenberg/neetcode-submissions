'''
Ordina gli intervalli per punto iniziale.
Mantieni nella stack l'intersezione del gruppo corrente.
Se due intervalli si sovrappongono, aggiorna l'ultimo con la loro intersezione.
Altrimenti, crea un nuovo gruppo.
'''
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        stack = []
        points.sort()

        def intersection(p1, p2):
            if p1[1] < p2[0]:
                return None
            return [
                max(p1[0], p2[0]),
                min(p1[1], p2[1])
            ]
        
        for point in points:
            if not stack:
                stack.append(point)
                continue
            
            inter = intersection(stack[-1], point)
            if inter:
                stack.pop()
                stack.append(inter)
            else:
                stack.append(point)
        
        return len(stack)
