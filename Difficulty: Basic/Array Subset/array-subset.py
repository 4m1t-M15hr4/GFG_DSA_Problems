class Solution:
    def isSubset(self, a, b):
        # code here
    
        d = {}
        for i in a:
            d[i] = d.get(i,0)+1
        for i in b:
            if i not in d:
                return False
            if d[i] == 0:
                return False
            d[i] = d.get(i,0) -1
        return True