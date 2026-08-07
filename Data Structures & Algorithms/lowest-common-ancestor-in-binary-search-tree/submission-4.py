# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pval = p.val
        qval = q.val
        radice = root
        while root:
            if pval >= root.val >= qval or pval <= root.val <= qval:
                return root
            elif root.val > pval and root.val > qval:
                root = root.left
            elif root.val < pval and root.val < qval:
                root = root.right

        return radice


