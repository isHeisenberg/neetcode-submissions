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

        def sameTree(p, q):
            if not p and not q:
                return True
            if (not p and q) or (p and not q) or p.val != q.val:
                return False

            return sameTree(p.left, q.left) and sameTree(p.right, q.right)
    
        if not root:
            return False

        if sameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)





