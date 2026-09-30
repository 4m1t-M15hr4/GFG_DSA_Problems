class Solution:
    def rearrange(self,arr):
        res =[]
        # code here
        pos = []
        neg = []
        for i in arr:
            if i >= 0:
                pos.append(i)
            else:
                neg.append(i)
        posIdx = 0
        negIdx = 0
        i = 0
        
        while posIdx < len(pos) and negIdx < len(neg):
            if i % 2 == 0:
                arr[i] =pos[posIdx]
                posIdx += 1
            else:
                arr[i] = neg[negIdx]
                negIdx +=1
            i += 1
        while posIdx < len(pos):
            arr[i] = pos[posIdx]
            posIdx += 1
            i += 1
        
        while negIdx < len(neg):
            arr[i] = neg[negIdx]
            negIdx += 1
            i += 1
         
        