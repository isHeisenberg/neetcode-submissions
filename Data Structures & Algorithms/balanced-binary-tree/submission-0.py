# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # la funzione qui è booleana, tuttavia non riesco ad avere una
    # sola funzione ricorsiva per farlo, quindi
    # creo funzione interna ricorsiva e ne uso risultato
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # qui posso calcolare delle altezze
        def height(node):
            if not node:
                return 0
            
            left = height(node.left)
            if left == -1:
                return -1
            
            right = height(node.right)
            if right == -1:
                return -1
            
            # se un qualsiasi subtree è unbalanced, lancio -1
            # e lo propago fino alla fine
            if abs(left - right) > 1:
                return -1
            
            return 1 + max(left, right)
        
        return height(root) != -1


