class Solution:
    def valEqualToPos(self, arr):
        res = []
        for i in range(len(arr)):
            if arr[i] == i +1:
                res.append(arr[i])
        return res