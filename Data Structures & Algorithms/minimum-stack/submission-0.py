    # è un approccio che non funziona, se faccio tanti push
    # e poi tanti pop, dovrei ricalcolare con O(n) il minimo anche dopo il secondo
    # DEVO SALVARMI SEMPRE IL MINIMO FINO A QUEL PUNTO! -> (val, min_current)

    # def __init__(self):
    #     self.minimum = None
    #     self.secondMinimum = None
    #     self.values = []

    # def push(self, val: int) -> None:
    #     self.values.append(val)
    #     if self.minimum > val:
    #         self.secondMinimum = self.minimum # non funziona
    #         self.minimum = val 



class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack:
            minimo = min(val, self.stack[-1][1])
        else:
            minimo = val
        self.stack.append((val, minimo))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        
