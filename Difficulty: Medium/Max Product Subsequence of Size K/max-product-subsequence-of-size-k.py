class Solution:
    def maxProduct(self, arr: list[int], k: int) -> int:
        n = len(arr)
        arr.sort()
        product = 1
        if arr[n - 1] == 0 and  (k & 1):
            return  0
        
        if arr[n -1] <= 0 and (k & 1):
            for i in range(n-1, n - k - 1, -1):
                product *= arr[i]
            return product
        left = 0
        right = n -1
        
        if k & 1:
            product *= arr[right]
            right -= 1
            k -= 1
        k //= 2
        
        for i in range(k):
            leftProduct = arr[left] * arr[left +1]
            rightProduct = arr[right] * arr[right - 1]
            
            if leftProduct > rightProduct:
                product *= leftProduct
                left +=2
            else:
                product *= rightProduct
                right -= 2
        return product
        
        # code here
