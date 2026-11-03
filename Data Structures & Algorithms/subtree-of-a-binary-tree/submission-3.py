'''
SUBTREE OF ANOTHER TREE - SERIALIZATION

Idea:
- Trasformo entrambi gli alberi in liste usando preorder (Root, Left, Right).
- Verifico se la lista di subRoot è contenuta in quella di root.

Perché aggiungere "#":
- Rappresenta un nodo None (figlio mancante).
- Preserva la struttura dell'albero.
- Senza "#", alberi diversi potrebbero avere la stessa traversal.
  Es: 1 con figlio sinistro 2 vs 1 con figlio destro 2
  Entrambi diventerebbero [1, 2], ma con "#" sono distinti.

Serialization:
- Nodo esistente -> aggiungo il valore.
- Nodo None -> aggiungo "#".
- Visito ricorsivamente sinistra e destra.

Ricerca:
- Posso usare "in" sulle stringhe serializzate oppure
  implementare manualmente la ricerca della sottolista.
- Complessità worst case: O(N * M).

N = nodi di root, M = nodi di subRoot.
'''
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        albero = []
        sottoAlbero = []

        def serialize(root):
            arr = []

            def dfs(node):
                if not node:
                    arr.append("#")
                    return

                arr.append(str(node.val))
                dfs(node.left)
                dfs(node.right)

            dfs(root)
            return arr

        albero = serialize(root)
        sottoAlbero = serialize(subRoot)

        return "".join(sottoAlbero) in "".join(albero)









