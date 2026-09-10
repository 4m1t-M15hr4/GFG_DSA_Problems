class Solution:
    def getOddOccurrence(self, arr):
        # code here 
        d  = {}
        for i in arr:
            d[i] =d.get(i,0) +1
        for key, value in  d.items():
            if value % 2 != 0:
                return key
          