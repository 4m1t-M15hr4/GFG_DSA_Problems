class Solution:
    def findElements(self,arr):
        n = len(arr)
        sorted_arr = sorted(arr)
        res =[]
        for i in range(n - 2):
            res.append(sorted_arr[i])
        return res
        
        # code here
    
