
class Node:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None
        
def inorder(curr, prev, ans):
    if curr is None:
        return 
    inorder(curr.left, prev, ans)
    if prev[0] is not None:
        ans[0] = min(ans[0], curr.data- prev[0].data)
    prev[0] = curr
    inorder(curr.right, prev, ans)

class Solution:
    def absDiff(self, root):
        
        # code here
        prev = [None]
        ans = [float('inf')]
        inorder(root, prev, ans)
        
        return ans[0]