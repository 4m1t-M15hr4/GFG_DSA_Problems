class Solution:
    def getAlternates(self, arr):
        res = []
        # Code Here
        for i in range(0 , len(arr), 2):
            res.append(arr[i])
        
            
        return res