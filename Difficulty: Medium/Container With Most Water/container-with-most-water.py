class Solution:
    def maxWater(self, arr):
        
        # code here
        n = len(arr)
        i = 0
        j = n - 1
        res = []
        while i < j or n != 0:
            if arr[i] <= arr[j]:
                res.append((j -i)  * arr[i])
                i += 1
            elif arr[i] > arr[j]:
                res.append(( j - i) * arr[j])
                j -= 1
            n -= 1
        return max(res)