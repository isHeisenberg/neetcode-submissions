'''
DETECT SQUARES - HASHMAP

- HashMap: (x, y) -> frequenza del punto.
- Itero sulle coordinate distinte, evitando una lista separata.
- Uso il punto diagonale rispetto alla query per identificare il quadrato.
- Verifico abs(px - x) == abs(py - y): stessa distanza su entrambi gli assi.
- Escludo x == px e y == py: il punto deve essere realmente diagonale.
- Gli altri due vertici sono (x, py) e (px, y).

PERCHÉ USARE LA DIAGONALE:
- Identifica univocamente i quattro vertici del quadrato.
- Non devo distinguere sopra/sotto o destra/sinistra.
- Evito di contare lo stesso quadrato più volte.

DUPLICATI:
- Moltiplico le frequenze dei tre punti aggiuntivi.
- Se itero su una lista con duplicati, la frequenza del diagonale
  è già conteggiata dal ciclo.
- Se itero sulle chiavi della HashMap, devo moltiplicarla esplicitamente.

COMPLESSITÀ:
- add: O(1) medio.
- count: O(N) medio, N = coordinate distinte.
'''
class CountSquares:
    def __init__(self):
        self.ptsCount = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point

        for x, y in self.ptsCount:
            # Si trova su stessa diagonale SSE
            # abs(py - y) != abs(px - x) IMPORTANTE
            # inoltre check che non sia lo stesso punto!
            if abs(py - y) != abs(px - x) or x == px or y == py:
                continue

            # combinazioni le trovo moltiplicando le frequenze!
            res += (
                self.ptsCount[(x, y)] *
                self.ptsCount.get((x, py), 0) *
                self.ptsCount.get((px, y), 0)
            )

        return res











'''
Usando anche una lista

class CountSquares:
    def __init__(self):
        self.ptsCount = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.pts:
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue
            # non moltiplico per il freq della diagonale, pk ce l'ho in pts!
            res += self.ptsCount.get((x, py), 0) * self.ptsCount.get((px, y), 0)
        return res
'''