class Solution:
    def alternateSort(self, arr):
        # code here
        n = len(arr)
        arr.sort()
        res = []
        i = 0
        j = n -1 
        while i < j:
            res.append(arr[j])
            j -= 1
            res.append(arr[i])
            i +=1
        if n % 2 != 0:
            res.append(arr[i])
        return res
        
            