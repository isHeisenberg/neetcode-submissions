# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []

        def dfs(node):
            if not node:
                return

            # in-order: LEFT-NODE-RIGHT (parto col più piccolo in ordine)
            dfs(node.left)
            arr.append(node.val)    # SALVO IN ARRAY
            dfs(node.right)

        dfs(root)
        return arr[k - 1]


        
        