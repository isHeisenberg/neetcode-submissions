# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        queue = deque()
        queue.append(root)

        # uso un bfs
        while queue:
            lunghezza = len(queue)
            somma = 0
            for _ in range(lunghezza):
                node = queue.popleft()
                somma += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            heapq.heappush(heap, -somma)
        
        if k > len(heap):
            return -1

        for _ in range(k):
            somma = heapq.heappop(heap)
        
        return -somma

















