# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diametro = 0

        def dfs(node):
            if not node:
                return 0
            
            sinistra = dfs(node.left)
            destra = dfs(node.right)

            # aggiorno il diametro
            self.diametro = max(self.diametro, sinistra + destra)

            # restituisco l'altezza
            return 1 + max(sinistra, destra)

        dfs(root)
        return self.diametro
        