class Solution:
    def segregateElements(self, arr):
        
        pos = [x for x in arr if x >= 0]
        neg = [x for x in arr if x < 0]
        
        arr[:] = pos + neg