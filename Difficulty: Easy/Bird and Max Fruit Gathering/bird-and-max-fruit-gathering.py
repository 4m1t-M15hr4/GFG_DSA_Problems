class Solution:

    def maxFruits(self, arr: list[int], m: int) -> int:
        
        n = len(arr)
        sum = 0
        for i in range(m):
            sum += arr[i]
            
        res = sum
        left = 0
        for right in range(m, n + m):
            sum -= arr[left]
            sum += arr[right % n]
            res = max(res, sum)
            left +=1
        return res
                
