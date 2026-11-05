# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        # ricorda il base case no nodi
        if not root:
            return arr
        
        # faccio BFS prendendo ultimo elemento di ogni livello
        q = deque()
        q.append(root)
        while q:
            lunghezza = len(q)
            for _ in range(lunghezza):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            arr.append(node.val)

        return arr















