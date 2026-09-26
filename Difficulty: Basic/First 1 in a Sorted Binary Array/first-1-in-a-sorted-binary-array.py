class Solution:
    def firstIndex(self, arr):
        for i in range(len(arr)):
            if arr[i] == 1:
                return i
        return -1
        # code here

