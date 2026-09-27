class Solution:
    def maxPerimeter(self, arr):
        #code here.
        n = len(arr)
        arr.sort(reverse=True)
        for i in range(n -2):
            if arr[i] < arr[i +1] + arr[i +2] :
                return arr[i] + arr[i +1] + arr[i +2]
        return -1