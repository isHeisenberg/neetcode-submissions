class Solution:
    # uso contatori in dict con pattern produttore-consumatore
    def isAnagram(self, s: str, t: str) -> bool:
        # chiaro controllo sulla lunghezza delle parole
        if len(s) != len(t):
            return False
        
        # così definisco un dizionario (per set devo fare set())
        count = {}
        
        # prima ciclo su tutta la stringa s
        for c in s:
            # se c esiste prende il valore, altrimenti pone a 0
            count[c] = count.get(c, 0) + 1
        
        # poi ciclo su tutta la stringa t
        for c in t:
            # se proprio non c'è c false, altrimenti se count già arrivato a 0, allora ho di più in t della stessa lettera
            if c not in count or count[c] == 0:
                return False
            count[c] -= 1
        
        return True

        # return set(s) == set(t)