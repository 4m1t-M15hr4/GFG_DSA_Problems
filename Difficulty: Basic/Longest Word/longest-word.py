class Solution:
    def longest(self, arr):
        # code here
        longs = arr[0]
        for i in range(1, len(arr)):
            if len(arr[i]) > len(longs):
                longs = arr[i]
        return longs