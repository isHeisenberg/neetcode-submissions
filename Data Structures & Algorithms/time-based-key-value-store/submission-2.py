from collections import defaultdict

class TimeMap:

    # creo un dict di liste di tuple key: (timestamp, value)
    def __init__(self):
        self.store = defaultdict(list) #dict con appese delle liste

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        lista = self.store[key]
        l, r = 0, len(lista) - 1
        # Returns a value such that set was called previously, with 
        # timestamp_prev <= timestamp. If there are multiple such values, 
        # it returns the value associated with the largest timestamp_prev
        res = ""

        while l <= r:
            mid = (l+r) // 2

            if (lista[mid][0] == timestamp):
                return lista[mid][1]
            
            if (lista[mid][0] < timestamp):
                res = lista[mid][1]
                l = mid + 1
            else:
                r = mid - 1

        return res


        
