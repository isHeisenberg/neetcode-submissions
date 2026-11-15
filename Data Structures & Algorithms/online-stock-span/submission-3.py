'''
Stack monotono decrescente (prezzo, span).

- Rimuovo dallo stack i prezzi <= prezzo attuale.
- Sommo gli span degli elementi rimossi.
- Inserisco (prezzo attuale, span totale).

Ogni elemento entra ed esce dallo stack una sola volta:
O(1) ammortizzato per next().
'''
class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1 
        while self.stack and self.stack[-1][0] <= price:
            _, s = self.stack.pop()
            span += s
        self.stack.append((price, span))
        return span