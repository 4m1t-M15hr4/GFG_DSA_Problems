class Solution:
    def formPyramid(self, arr):
        # code here 
        n = len(arr)
        totalHeight = 0
        for i in range(n):
            totalHeight += arr[i]
        
        if n <= 2:
            return totalHeight - 1
        left = [0] *n
        right = [0] *n
        
        left[0] = 1
        for i in range(1, n):
            left[i] = min(left[i - 1] + 1, arr[i])
        
        right[n -1] = 1
        for i in range(n -2, -1, -1):
            right[i] = min(right[i + 1]+ 1, arr[i])
        
        minCost = float('inf')
        
        for i in range(n):
            peakHeight = min(left[i], right[i])
            
            pyramidSum = peakHeight * peakHeight
            
            minCost = min(minCost, totalHeight - pyramidSum)
        return minCost