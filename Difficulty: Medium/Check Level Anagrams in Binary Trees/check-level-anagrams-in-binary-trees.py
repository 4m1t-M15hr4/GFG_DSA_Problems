from collections import deque

class Node:
    def __init__(self, x: int):
        self.data = x
        self.left = self.right = None


class Solution:

    def areAnagrams(self, root1, root2):
        """ code here """
        if root1 is None or root2 is None:
            return root1 is root2
        q1 = deque([root1])
        q2 = deque([root2])
        while q1 and q2:
            n1 = len(q1)
            n2 = len(q2)
            
            if n1 != n2:
                return False
            freq = {}
            
            for _ in range(n1):
                node1 = q1.popleft()
                node2 = q2.popleft()
                
                freq[node1.data] = freq.get(node1.data, 0) + 1
                freq[node2.data] = freq.get(node2.data, 0) - 1
                if node1.left is not None:
                    q1.append(node1.left)
                if node1.right is not None:
                    q1.append(node1.right)
                if node2.left is not None:
                    q2.append(node2.left)
                if node2.right is not None:
                    q2.append(node2.right)
            for value in freq.values():
                if value != 0:
                    return False
        return not q1 and not q2