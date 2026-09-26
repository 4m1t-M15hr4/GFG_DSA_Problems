class Solution:
    def firstSearch(self, arr, k):
        for i in range(len(arr)):
            if arr[i] == k:
                return i
        return -1
        