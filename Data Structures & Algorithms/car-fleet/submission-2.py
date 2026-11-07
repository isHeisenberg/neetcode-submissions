class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # (posizione, tempo per arrivare)
        cars = [ [position[i], (target - position[i]) / speed[i]] for i in range(len(position))]
        cars.sort(reverse=True)

        stack = []

        for car in cars:
            if not stack or car[1] > stack[-1][1]:
                stack.append(car)

        return len(stack)
