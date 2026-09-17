class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alphabet = {}

        for i in range(len(order)):
            alphabet[order[i]] = i

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            lunghezza = min(len(word1), len(word2))

            # FOR - ELSE
            # esegue l'else se il for termina normalmente senza break
            # Se ho confrontato tutte le lettere senza trovare una differenza, 
            # allora le parole sono uguali fino alla lunghezza della più corta
            for j in range(lunghezza):
                if alphabet[word1[j]] > alphabet[word2[j]]:
                    return False

                if alphabet[word1[j]] < alphabet[word2[j]]:
                    break
            else:
                # Tutti i caratteri confrontati sono uguali.
                # Quindi word1 non può essere più lunga di word2.
                if len(word1) > len(word2):
                    return False

        return True

