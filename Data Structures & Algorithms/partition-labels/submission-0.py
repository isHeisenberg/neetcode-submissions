'''
GREEDY:
Prendo substring fino al max continuando ad aggiornarlo
in base alle lettere che ho dentro la substring
"xyxxyzbzbbisl"
x: 3 y: 4 z: 7 b: 9 i: 10 s: 11 l: 12
'''
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # dict -> lettera: ultima_pos
        ends = {}
        for idx, letter in enumerate(s):
            ends[letter] = idx
        
        l, r = 0, 0
        res = []
        for i in range(len(s)):
            r = max(r, ends[s[i]])

            if i == r:
                res.append(r - l + 1)
                l = i + 1

        return res

        


        
        