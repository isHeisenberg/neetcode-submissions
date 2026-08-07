# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # node.left < node < node.right non basta, infatti magari sotto soddifa
        # la condizione del minore, ma è maggiore della root ad esempio
        def dfs(node, low, high):
            if not node:
                return True
            
            if not (low < node.val < high):
                return False
            '''
            LEFT: Tutti i nodi a sinistra devono essere < node.val. Quindi:
                low resta uguale
                high diventa node.val   
            '''
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
        
        return dfs(root, float("-inf"), float("inf")) # usare i float("inf")




