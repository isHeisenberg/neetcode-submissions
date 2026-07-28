class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            count = [0] * 26              # array di 26 zeri, uno per ogni lettera

            for c in s:
                count[ord(c) - ord('a')] += 1   # incrementa il contatore della lettera

            key = tuple(count)            # converte la lista in tuple (hashabile)
            groups[key].append(s)         # aggiunge la parola al gruppo corrispondente

        return list(groups.values())      # restituisce tutti i gruppi