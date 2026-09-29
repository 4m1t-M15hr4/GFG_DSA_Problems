class Solution:
    def findUnion(self, a, b):
        # code here 
        n, m = len(a), len(b)
        
        res = []
        i, j = 0, 0
        while i < n and j < m:
            if i > 0 and  a[i - 1] == a[i]:
                i +=1
                continue
            if j  > 0 and b[j -1] == b[j]:
                j += 1
                continue
            if a[i] > b[j]:
                res.append(b[j])
                j += 1
            elif a[i] < b[j]:
                res.append(a[i])
                i +=1
            
            else:
                res.append(a[i])
                i +=1
                j += 1
        while i < n :
            if i > 0 and a[i-1] == a[i]:
                i +=1
                continue
            res.append(a[i])
            i += 1
        while j < m:
            if j > 0 and b[j -1] == b[j]:
                j +=1
                continue
            res.append(b[j])
            j +=1
        return res