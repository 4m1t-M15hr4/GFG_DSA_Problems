class Solution:
    def binarySearch(self, arr, k):
        # code here
        l = 0
        h = len(arr) - 1
        while l <= h:
            mid = l + (h -l) // 2
            if arr[mid] == k:
                return True
            elif arr[mid] < k:
                l = mid +1
            else:
                h = mid -1 
        return False