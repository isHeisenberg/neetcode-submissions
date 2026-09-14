# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root:
            return TreeNode(val)
            
        def dfs(root, val):
            if not root:
                return True

            if val > root.val:
                if dfs(root.right, val):
                    root.right = TreeNode(val)
            else:
                if dfs(root.left, val):
                    root.left = TreeNode(val)

            return False

        dfs(root, val)
        return root





            