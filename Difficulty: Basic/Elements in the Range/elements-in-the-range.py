class Solution:
    def checkElements(self, start, end, arr):
        st = set(arr)
        for i in range(start, end + 1):
            if i not in st:
                return False
        return True
        # code here
        
