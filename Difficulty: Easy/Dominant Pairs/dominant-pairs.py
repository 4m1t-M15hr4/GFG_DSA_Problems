class Solution:
    def dominantPairs(self, arr: list[int]) -> int:
        
        n = len(arr)
        arr[:n//2] = sorted(arr[:n//2])
        arr[n//2:] = sorted(arr[n//2:])
        # code here
        cnt = 0
        rgt = n //2
        
        for lft in range(n //2):
            while rgt < n and arr[lft] >= 5 *arr[rgt]:
                rgt += 1
                
            cnt += (rgt - n // 2)
        return cnt