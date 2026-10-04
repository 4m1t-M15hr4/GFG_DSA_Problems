class Solution:
    def find(self, arr, x):
        # code here
        l = 0
        r = len(arr) - 1
        ans = -1 
        
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid] == x:
                ans = mid
                r = mid -1 
                
                
                
            elif arr[mid] < x:
                l = mid + 1
            elif arr[mid] > x:
                
                r = mid -1
        if ans == -1:
            return [-1,-1]
        l = ans
        r = len(arr) - 1
        ans2 = -1
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid] == x:
                ans2 = mid
                l = mid  +1
            elif arr[mid] < x:
                l = mid +1
            elif arr[mid] > x:
                r = mid - 1
        return [ans, ans2]
            
        