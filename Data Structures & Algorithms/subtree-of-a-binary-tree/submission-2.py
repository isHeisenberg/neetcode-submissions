# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        albero = []
        sottoAlbero = []

        def serialize(root):
            arr = []

            def dfs(node):
                if not node:
                    arr.append("#")
                    return

                arr.append(str(node.val))
                dfs(node.left)
                dfs(node.right)

            dfs(root)
            return arr

        albero = serialize(root)
        sottoAlbero = serialize(subRoot)

        return "".join(sottoAlbero) in "".join(albero)









