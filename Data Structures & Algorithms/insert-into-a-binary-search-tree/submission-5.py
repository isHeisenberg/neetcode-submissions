# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr = root
        newNode = TreeNode(val)
        if not curr:
            return newNode

        while curr:
            if curr.val > val:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = newNode
                    return root
            else:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = newNode
                    return root
        


            