# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return None

        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        if not root.left and not root.right and root.val == target:
            return None

        return root




'''
class Solution(...):
    def dfs(root):
        if not root:
            return None

        # 2. Controlli se il nodo è una foglia troppo presto
        # Ma un nodo potrebbe diventare una foglia dopo aver eliminato i suoi figli.
        if root.val == target and not root.left and not root.right:
            return None

        # 1. Non aggiorni i figli del nodo
        # Anche se la chiamata ricorsiva restituisce None, tu ignori il valore restituito.
        self.removeLeafNodes(root.left, target)
        self.removeLeafNodes(root.right, target)

    dfs(root)
    return root
'''


