'''
Trie + DFS + Backtracking

- Trie: permette di cercare più parole contemporaneamente.
- DFS: esplora tutte le direzioni partendo da ogni cella.
- Backtracking: evita di riutilizzare una cella nello stesso percorso,
  rimuovendola da visit quando si torna indietro.

node rappresenta il nodo corrente del Trie.
word rappresenta la parola costruita lungo il percorso.
Se una lettera non esiste nei children del Trie, interrompiamo subito
quel percorso (pruning).
Se node.isWord è True, abbiamo trovato una parola.

visit è condiviso tra le chiamate DFS, ma viene ripulito
dopo ogni esplorazione grazie al backtracking.
res è un set per evitare duplicati.
'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        # visit dichiaro fuori, tanto backtrack me la svuota ogni volta!
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or r >= ROWS or
                c >= COLS or (r, c) in visit or
                board[r][c] not in node.children
            ):
                return

            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)


        