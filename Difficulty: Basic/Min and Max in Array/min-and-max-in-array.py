class Solution:
    def getMinMax(self, arr):
        mn = float('inf')
        mx = float('-inf')
        

        for num in arr:
            if num < mn:
                mn = num
            if num > mx:
                mx = num
        return [mn, mx]