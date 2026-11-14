'''
TREE RECURSION - CONCETTI FONDAMENTALI

1. RETURN: informazione che SALE (figli -> padre)
   - Il figlio restituisce un risultato al padre.
   - Il padre può raccoglierlo con: left = dfs(node.left).
   - Utile quando un nodo deve sapere cosa è stato trovato nei
     sottoalberi (es. altezza, LCA, diametro).
   - Senza return di un valore, la funzione restituisce None.

2. NO RETURN: esecuzione che RISale, ma nessun dato
   - Quando una chiamata termina, l'esecuzione torna sempre al padre.
   - Ma se non restituisco un valore, il padre non riceve
     informazioni utili dal figlio.
   - Esempio: dfs(node.left) senza assegnamento.
   - Utile quando devo solo visitare nodi, stampare o modificare
     una variabile condivisa.

3. ARGOMENTI: informazione che SCENDE (padre -> figli)
   - Passo ai figli informazioni già raccolte lungo il percorso.
   - Esempio: dfs(node.left, depth + 1).
   - Utile per profondità, somme dei cammini e path tracking.

4. VARIABILI CONDIVISE (nonlocal / self)
   - Permettono di salvare un risultato accessibile da tutte
     le chiamate ricorsive.
   - Esempio: nonlocal lca; lca = node.
   - Non servono a restituire informazioni ai genitori.

5. CONTRATTO DELLA DFS
   - Prima di scrivere la ricorsione, chiediti:
     "Cosa deve restituire questa funzione per ogni sottoalbero?"
   - Il return deve avere un significato preciso.
   - Esempio LCA: True/False = ho trovato p/q nel sottoalbero.

6. POST-ORDER
   - Prima visito i figli, poi elaboro il nodo corrente.
   - Utile quando il nodo deve combinare i risultati dei figli.
   - Schema:
       left = dfs(node.left)
       right = dfs(node.right)
       # elaboro node usando left e right

7. FIDUCIA RICORSIVA
   - Quando scrivo left = dfs(node.left), assumo che la DFS
     del sottoalbero sinistro funzioni correttamente.
   - Non devo simulare tutta la ricorsione: penso solo a come
     usare il risultato restituito dai figli.

8. CASO BASE
   - Gestisce il punto in cui non posso più scendere.
   - Negli alberi: if not node.
   - Deve restituire un valore coerente con il contratto della DFS.

REGOLA MENTALE:
- Informazione che arriva dall'alto -> ARGOMENTI.
- Informazione che arriva dal basso -> RETURN.
- Risultato da salvare globalmente -> VARIABILE CONDIVISA.
- L'esecuzione risale sempre, ma il dato risale solo con RETURN.
'''
class Solution:
    def lowestCommonAncestor(
        self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'
    ) -> 'TreeNode':
        if root is None or root is p or root is q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        # Se hai trovato solo uno dei due, 
        # lo passi in alto e aspetti che un antenato trovi l'altro.
        return left if left else right


















'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.lca = None

        def dfs(root, pnode, qnode):
            if root == None:
                return
            
            if root == p:
                pnode = root
            if root == q:
                qnode = root
            
            if pnode and qnode:
                self.lca = root
                return
            
            # l'informazione sta andando solo da padri a figli
            # ma a me serve far risalire l'info
            # tipo avendo left = dfs(root.left, pnode, qnode)
            # con quindi dei return che diano qualcosa
            dfs(root.left, pnode, qnode)
            dfs(root.right, pnode, qnode)

        dfs(root, None, None)
        return self.lca
'''