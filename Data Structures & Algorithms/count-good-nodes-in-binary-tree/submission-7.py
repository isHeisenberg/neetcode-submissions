# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.counter = 0

        def dfs(root, maximum):
            if not root:
                return 

            if root.val >= maximum:
                self.counter += 1
            
            maximum = max(root.val, maximum)
            dfs(root.right, maximum)
            dfs(root.left, maximum)

        dfs(root, root.val)
        return self.counter
