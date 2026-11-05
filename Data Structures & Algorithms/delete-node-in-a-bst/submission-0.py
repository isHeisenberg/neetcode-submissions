# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)  # Aggiorna il sottoalbero destro
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)    # Aggiorna il sottoalbero sinistro
        else:
            # Nodo senza figlio sinistro: restituisci il destro (anche None)
            if not root.left:
                return root.right
            # Nodo senza figlio destro: restituisci il sinistro
            elif not root.right:
                return root.left

            # Due figli: trova il successore inorder (minimo nel sottoalbero destro)
            cur = root.right
            while cur.left:
                cur = cur.left

            root.val = cur.val  # Sostituisci il valore del nodo da eliminare
            root.right = self.deleteNode(root.right, root.val)  # Elimina il successore originale

        return root  # Restituisci il sottoalbero aggiornato al genitore


    
