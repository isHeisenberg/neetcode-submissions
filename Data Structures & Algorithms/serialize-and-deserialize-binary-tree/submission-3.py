# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        q = deque([root])
        res = []
        while q:
            node = q.popleft()
            if node:
                res.append(str(node.val))
                q.append(node.left)    # posso appendere None
                q.append(node.right)   # basta che poi questo dentro if
            else:
                res.append('N')
        return ','.join(res)

        
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(',')
        if vals[0] == 'N':
            return None

        '''
        Prendo un nodo dalla queue.
        Leggo il prossimo valore: è il figlio sinistro?
        Se non è N, creo il figlio e lo aggiungo alla queue.
        Leggo il prossimo valore: è il figlio destro?
        Se non è N, creo il figlio e lo aggiungo alla queue.
        Passo al prossimo nodo nella queue.
        '''
        root = TreeNode(int(vals[0]))
        queue = deque([root])
        index = 1
        while queue:
            node = queue.popleft()
            if vals[index] != "N":
                node.left = TreeNode(int(vals[index]))
                queue.append(node.left)
            index += 1
            if vals[index] != "N":
                node.right = TreeNode(int(vals[index]))
                queue.append(node.right)
            index += 1
        return root








