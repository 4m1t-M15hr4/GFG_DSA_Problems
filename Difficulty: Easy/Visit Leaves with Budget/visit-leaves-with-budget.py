from collections import deque
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def getCount(self, root, k):
        if root is None:
            return 0
        q = deque()
        q.append(root)
        
        level= 1
        cnt = 0
        while q:
            size = len(q)
            lcnt = 0
            
            for i in range(size):
                curr = q.popleft()
                if curr.left is None and curr.right is None:
                    lcnt += 1
                if curr.left is not None:
                    q.append(curr.left)
                if curr.right is not None:
                    q.append(curr.right)
            cnvst = k // level
            
            take = min(lcnt, cnvst)
            
            cnt += take
            k -= take * level
            
            if k < level:
                break 
            level +=1 
        return cnt
            
        # code here
        