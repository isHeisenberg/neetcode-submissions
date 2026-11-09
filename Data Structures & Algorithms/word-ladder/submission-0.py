class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        # 1) COSTRUZIONE DEL GRAFO
        # nei[pattern] = tutte le parole che corrispondono a quel pattern
        nei = defaultdict(list)
        wordList.append(beginWord)         
        for word in wordList:
            for j in range(len(word)):
                # sostituisco la lettera j con il jolly "*"
                pattern = word[:j] + "*" + word[j + 1:]
                nei[pattern].append(word)

        # 2) BFS
        visit = set([beginWord])          
        q = deque([beginWord])             
        res = 1                             
        while q:
            # processo UN LIVELLO alla volta: len(q) fissa quante parole
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res

                # genero i vicini tramite i pattern della parola
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)      
                            q.append(neiWord)

            res += 1                        

        return 0                           