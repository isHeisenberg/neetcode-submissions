# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root, maximum, minimum):
            if not root:
                return True

            if not (minimum < root.val < maximum):
                return False

            # a ogni step definisco il max e min di ognuno dei sottoalberi
            return dfs(root.left, root.val, minimum) and dfs(root.right, maximum, root.val)

        return dfs(root, float('inf'), float('-inf'))

