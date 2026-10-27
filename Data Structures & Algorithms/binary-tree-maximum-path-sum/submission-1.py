# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = [float('-inf')]  
        
        def dfs(root):
            if not root:
                return 0 # ramo vuoto: non aggiunge nulla
            
            # ⬇scendo, prendo il meglio offerto da ciascun ramo
            left = dfs(root.left)
            right = dfs(root.right)
            
            # se un ramo è negativo, meglio ignorarlo
            left = max(left, 0)
            right = max(right, 0)
            
            # candidato al massimo GLOBALE: uso ENTRAMBI i rami
            candidato = root.val + left + right
            max_sum[0] = max(max_sum[0], candidato)
            
            # cosa offro al mio padre: solo il MIGLIOR ramo singolo, non entrambi
            return root.val + max(left, right)
        
        dfs(root)
        return max_sum[0]

