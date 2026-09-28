class Solution:
    def findFloor(self, arr, x):
        # code here
        res = -1
        l = 0
        r = len(arr) - 1
        while l <= r:
            mid = l + ( r -l ) // 2
            if arr[mid] <= x:
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return res