class Solution:
    def mergeNsort(self, arr1, arr2):
        res =[]
        i = 0
        j = 0
        while i < len(arr1):
            res.append(arr1[i])
            i += 1
            
        while j < len(arr2):
            res.append(arr2[j])
            j +=1
        return sorted(set(res))
        # code here
        
